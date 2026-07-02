from pathlib import Path
import json

# Folder containing this script and the photos
folder = Path("./photos")

# Image extensions to include
extensions = {".jpg", ".jpeg", ".png", ".webp"}

students = []

for f in sorted(folder.iterdir()):
    if f.suffix.lower() in extensions:
        students.append({
            "name": f.stem,
            "image": f.name
        })

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Student Flashcards</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background:#f4f4f4;
    text-align:center;
    margin:0;
}}

#container {{
    max-width:700px;
    margin:auto;
    padding:20px;
}}

img {{
    max-width:90%;
    max-height:70vh;
    border-radius:12px;
    box-shadow:0 0 15px rgba(0,0,0,.3);
}}

#name {{
    font-size:36px;
    margin-top:20px;
    color:#2c3e50;
    visibility:hidden;
}}

button {{
    font-size:20px;
    padding:12px 24px;
    margin:10px;
}}

#counter {{
    font-size:18px;
    margin-top:10px;
}}

</style>

</head>

<body>

<div id="container">

<h2>Student Flashcards</h2>

<div id="counter"></div>

<img id="photo">

<div id="name"></div>

<br>

<button onclick="showName()">Reveal Name</button>

<button onclick="previousCard()">◀ Previous</button>

<button onclick="nextCard()">Next ▶</button>

<button onclick="shuffleDeck()">Shuffle</button>

</div>

<script>

const students = {json.dumps(students, indent=4)};

let order = [...Array(students.length).keys()];
let current = 0;

function loadCard() {{

    let student = students[order[current]];

    document.getElementById("photo").src = student.image;

    document.getElementById("name").innerHTML = student.name;

    document.getElementById("name").style.visibility = "hidden";

    document.getElementById("counter").innerHTML =
        (current+1) + " / " + students.length;

}}

function showName(){{
    document.getElementById("name").style.visibility="visible";
}}

function nextCard(){{
    current=(current+1)%students.length;
    loadCard();
}}

function previousCard(){{
    current=(current-1+students.length)%students.length;
    loadCard();
}}

function shuffleDeck(){{
    for(let i=order.length-1;i>0;i--){{
        let j=Math.floor(Math.random()*(i+1));
        [order[i],order[j]]=[order[j],order[i]];
    }}
    current=0;
    loadCard();
}}

document.addEventListener("keydown",function(e){{
    if(e.key=="ArrowRight") nextCard();
    if(e.key=="ArrowLeft") previousCard();
    if(e.key==" ") {{
        e.preventDefault();
        showName();
    }}
}});

loadCard();

</script>

</body>
</html>
"""

(Path(".") / "index.html").write_text(html, encoding="utf-8")

print(f"Created index.html with {len(students)} students.")