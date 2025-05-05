import asyncio
import socket
from types import TracebackType
from typing import Optional, Type


class ConnectedSocket:
    def __init__(self, server_socket):
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self):
        '''Эта сопрограмма вызывается
        при входе в блок with. Она ждет
        подключения клиента и возвращает
        это подключение'''

        print('Вход в контекстный менеджер, ожидание подключения')
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print(f'Подключение подтверждено {address}')
        return self._connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        '''  Эта сопрограмма вызывается при выходе
        из блока with. В ней мы производим
        очистку ресурса, В данном случае
        закрывается подключение'''

        print('Выход из контекстного менеджера')
        self._connection.close()
        print('Подключение закрыто')
        

'''
Здесь мы создали асинхронный контекстный менеджер ConnectedSocket. 
Этот класс принимает серверный сокет, и в сопрограмме
__aenter__ мы ждем подключения клиента. Как только клиент под-
ключился, возвращается соответствующее ему клиентское подклю-
чение. Это дает нам доступ к подключению в части as предложения
async with. Затем в блоке async with мы используем это подключение
для ожидания данных от клиента. Когда выполнение этого блока за-
вершается, вызывается сопрограмма __aexit__, которая закрывает
подключение.
'''
async def main():
    loop = asyncio.get_event_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
   
    async with ConnectedSocket(server_socket) as connection:  # Здесь вызывается __aenter__ и начинается ожидание подключения
        data = await loop.sock_recv(connection, 1024)
        print(data)  # После этого предложения вызывается __aexit__ и подключение закрывается


asyncio.run(main())