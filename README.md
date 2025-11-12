# ConnectX 🎥💬

A modern, professional **video conferencing web application** built with Django. ConnectX allows users to create meetings, join rooms, and chat seamlessly — similar to Google Meet.

---

## Features ✅

- User registration and login **via email**  
- Create or join video meetings  
- User dashboard with meeting management  
- Responsive design for **desktop and mobile**  
- Full-screen video call support  
- Clean and professional UI/UX inspired by modern conferencing apps  
- Email-based authentication ensures security and simplicity  
- Friendly user interface with smooth animations  
- Join meetings via Room ID instantly  
- Logout securely from any device  
- **Real-time video and audio calls powered by ZegoCloud**

---

## Technology Stack 🛠️

- **Backend:** Django  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Database:** SQLite (default Django)  
- **Authentication:** Email-based login with full name  
- **Video/Audio Calls:** ZegoCloud Web SDK  
- **Other:** Django messages framework, static files for CSS  

---

## Installation 💻

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/ConnectX.git
cd ConnectX
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional for admin access):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Usage 🚀

- Register a new account using your **email and full name**  
- Login using your **email and password**  
- Access the **dashboard**:  
  - **New Meeting** → Create a new video room  
  - **Join Meeting** → Enter a Room ID to join an existing meeting  
  - **Logout** → Exit your account  
- Video calls are powered by **ZegoCloud** for real-time audio/video communication

---

## ZegoCloud Integration 🌐

ConnectX uses **ZegoCloud** for real-time video and audio calls.  

- Low-latency, high-quality video calls  
- Join or create rooms with unique Room IDs  
- Secure token-based authentication for all users

### Frontend (videocall.html)

```html
<script src="https://cdn.zego.im/zego-uikit-web-2.8.1.js"></script>
<div id="video-container"></div>
<script>
const appID = <YOUR_ZEGOCLOUD_APP_ID>;
const serverSecret = '<YOUR_SERVER_SECRET>';
const userID = '{{ user.id }}';
const userName = '{{ user.get_full_name }}';
const roomID = '{{ room_id }}';

const zp = new ZegoUIKitPrebuilt();
zp.joinRoom({
    container: document.getElementById('video-container'),
    scenario: 'VideoCall',
    roomID: roomID,
    userID: userID,
    userName: userName,
    token: generateToken(appID, serverSecret, roomID, userID),
});
</script>
```

### Backend Token Generation

```python
from django.http import JsonResponse
from zego_sdk import ZegoToken

def generate_token(request):
    user_id = request.user.id
    room_id = request.GET.get('roomID')
    token = ZegoToken(app_id=<APP_ID>, server_secret='<SECRET>').generate_token(user_id, room_id)
    return JsonResponse({'token': token})
```

[Learn more about ZegoCloud](https://www.zegocloud.com/)

---

## Folder Structure 📁

```
ConnectX/
├── ConnectX/       # Django project
├── accounts/       # App for authentication
├── templates/      # HTML templates
├── static/         # CSS, JS, images
├── manage.py
└── requirements.txt
```

---

<!-- ## Demo 🎬

Watch the ConnectX demo here:  
[![Watch the demo](https://img.youtube.com/vi/<VIDEO_ID>/0.jpg)](https://www.youtube.com/watch?v=<VIDEO_ID>) -->

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing 🤝

- Fork the repository  
- Create a new branch (`git checkout -b feature-name`)  
- Commit your changes (`git commit -m 'Add feature'`)  
- Push to the branch (`git push origin feature-name`)  
- Open a Pull Request  

---

## Contact ✉️

- Developer: Md Jahid Hasan  
- Email: jahidhasanpiyesh@gmail.com  
- LinkedIn: [https://www.linkedin.com/in/md-jahid-hasan-9418b9298](https://www.linkedin.com/in/md-jahid-hasan-9418b9298)  
- Portfolio: [https://jahidhasanpiyesh.github.io/](https://jahidhasanpiyesh.github.io/)  
