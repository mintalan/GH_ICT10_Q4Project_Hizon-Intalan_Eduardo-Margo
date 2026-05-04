from pyscript import document

gallery = document.getElementById("gallery")

gallery.innerHTML = """
<div class="photo">
    <img src="photo1.jpg">
    <p>Halloween</p>
</div>

<div class="photo">
    <img src="photo2.jpg">
    <p>Food Fair</p>
</div>

<div class="photo">
    <img src="photo3.jpg">
    <p>Random Moments in Sapphire</p>
</div>
"""