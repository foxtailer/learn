document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('report_btn').addEventListener('click', function() {
        console.log('fff')
        const postId = this.getAttribute('data-post-id');
        const button = this;
    
        button.disabled = true;
    
        fetch('{% url "main:report" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: new URLSearchParams({
                'post_id': postId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('Report incremented. New report count:', data.report);
            } else {
                console.error('Error:', data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

});