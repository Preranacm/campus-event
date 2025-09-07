from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Campus Event Management</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #74ebd5, #ACB6E5);
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 900px;
                margin: 50px auto;
                background: rgba(255,255,255,0.95);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 20px;
            }
            p {
                text-align: center;
                color: #555;
                font-size: 1.1em;
                margin-bottom: 30px;
            }
            .api-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 15px;
            }
            .api-card {
                background: #f5f5f5;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                transition: 0.3s;
                font-weight: bold;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            .api-card:hover {
                background: #333;
                color: #fff;
                transform: translateY(-5px);
            }
            .api-card a {
                text-decoration: none;
                color: inherit;
                display: block;
            }
            .icon {
                font-size: 2em;
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Campus Event Management</h1>
            <p>Click any card below to test the backend APIs directly:</p>
            <div class="api-grid">
                <div class="api-card"><a href="/api/colleges/" target="_blank"> Colleges</a></div>
                <div class="api-card"><a href="/api/students/" target="_blank"> Students</a></div>
                <div class="api-card"><a href="/api/events/" target="_blank">Events</a></div>
                <div class="api-card"><a href="/api/registrations/" target="_blank"> Registrations</a></div>
                <div class="api-card"><a href="/api/attendance/" target="_blank"> Attendance</a></div>
                <div class="api-card"><a href="/api/feedback/" target="_blank"> Feedback</a></div>
                <div class="api-card"><a href="/api/reports/event-popularity/" target="_blank">Event Popularity</a></div>
                <div class="api-card"><a href="/api/reports/student-participation/" target="_blank"> Student Participation</a></div>
                <div class="api-card"><a href="/api/reports/top-students/" target="_blank"> Top 3 Students</a></div>
                <div class="api-card"><a href="/api/reports/event-feedback/" target="_blank"> Event Feedback</a></div>
            </div>
        </div>
    </body>
    </html>
    """)
