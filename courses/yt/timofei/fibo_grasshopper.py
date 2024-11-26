"""найти все возможные траектории прыжка по 1 или по 2 до точки n"""
#  Kn = Kn-2 + Kn-1

#  baned dots
#  + 3dot step

N = 6
traj = [0,1] + [0]*(N-1)
print(traj)
for i in range(2, N+1):
    traj[i] = traj[i-1]+traj[i-2]
print(traj[N])

def count_trajectories(allowed:list):
    N = len(allowed)
    k = [0, 1, int(allowed[2])] + [0] * (N-3)
    for i in range(3, N):
        if allowed[i]:
            k[i] = k[i-1] + k[i-2] + k[i-3]
    return k[N-1]

dots = [1] * 100
dots[5] = 0
dots[54] = 0
dots[37] = 0
dots[84] = 0

print(count_trajectories(dots))