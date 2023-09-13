from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return html

style = """
header {
    height: 100px;
    box-shadow: 10px 10px 18px 0px black;
}

header a {
    text-decoration: none;
    margin-top: auto;
    display: flex;
    justify-content: center;
    align-items: center;
}
header a:hover {
    text-decoration: underline;
    color: rgb(163, 33, 33);
}
header img {
    size: 20px;
    width: 100px;
}
header img:hover {
    background-color: rgb(163, 33, 33);
}
body {
    background-image: url("assets/img/background.jpg");
    font-family: 'Courier New', Courier, monospace;
}
div {
    background-color: rgba(255, 255, 255, 0.466);
}
p {
    font-family: 'Courier New', Courier, monospace;
}
h1 {
    
}
"""
html = f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>{style}</style>
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