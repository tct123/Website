from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return html

html = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="style.css" media="screen" />
    <audio src="assets/sound/sound.mp3" autoplay></audio>
</head>
<body>
    <header>
        <!--<img src="assets/img/Zeichnung.svg" alt="Logo">-->
        <a href="https://github.com/tct123">GitHub</a>
        <a href="https://www.youtube.com/channel/UC4gYuC-XcTNSj42ZsHJSJ1Q">TCTDiy (YouTube)</a>
        <a href="https://twitter.com/tctdiy_gaming">Twitter</a>
    </header>
    <div>
        <h1>Über mich</h1>
        <p>Hallo</p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FM2PGAOO29Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    <div>
        <h2 class="header">Header2</h2>
        <video src="assets/vid/tct-diy-intro.mp4" width="560" height="315"></video>
    </div>
</body>
</html>
"""
app.run()