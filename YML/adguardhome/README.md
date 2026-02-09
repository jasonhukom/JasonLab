<!DOCTYPE html>
<html>
    <head>
        <title>AdGuardHome dockercompose.yaml README</title>
            <style>
        code {
            background-color: #eee;
            border: 1px solid #999;
            display: block;
            padding: 10px;
            white-space: pre-wrap;
        }
    </style>
    </head>
    <body>
        <h1>AdGuardHome</h1>
        <p>Open the initial setup wizard and admin UI HTTP</p>
        <code>  ports:
      #--- Listining Ports ---
      - "53:53/tcp"       # DNS
      - "53:53/udp"       # DNS
      - "3000:3000/tcp"   # Initial Setup Wizzard
      - "8080:80/tcp"   # Admin UI HTTP</code>
</html>