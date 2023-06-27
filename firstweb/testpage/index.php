<!DOCTYPE html>
<html>
	<head>
			<title>Blog</title>
			<link rel="stylesheet" href="style.css">
			<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
			<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
			<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">
	</head>
	<body>
		<header>
			<h1>"NoSad" Blogo <div id="right" title="This phrase will be on the right side of the page."><p> &copy </p></div></h1>
			<nav>
				<ul>
					<li><a href="#pages">Pages</a></li>
					<li><a href="#work">Work</a></li>
					<li><a href="#js">JavaScript</a></li>
					<li><a href="#contact">Contact</a></li>
				</ul>
			</nav>
		</header>
		<article class="arttime">
			<div class="wrapper">
       			<div class="display">
            		<div id="time"></div>
        		</div>
        		<span></span>
        		<span></span>
    		</div>
		</article>
		<div class="headset">
			<img src="img/headset1.png" alt="">
			<!-- <img src="img/headset2.png" alt="">
				 <img src="img/headsetlama1.png" alt="">
				 <img src="img/headsetlama2.png" alt=""> -->
				<div class="priceh">Only today 13.99$</div>
		</div>
		<button class="glassef">Third Page</button>
		<main>
			<button id="npage1" class="phome">Home</button>
			<section id="pages">
				<h2>Pages</h2>
					<!-- Для открытия в новой вкладке target="_blank" -->
				<p class="center-text"> This can be attributed to a link in the text to your resource -<a href="index.php">Just Second Page</a></p>
				<button id="npage3" class="npage3">Third Page</button>
				<p class="center-text">
					<div class="page-number"><span>2</span></div> <!-- page number -->
					- Current page
				</p>
			</section> 
			<section id="work">
				<h2>My Work</h2>
				<div class="gallery">
					<img src="img/img1.jpg" alt="Work 1">
					<img src="img/img2.jpg" alt="Work 2">
					<img src="img/img3.jpg" alt="Work 3">
					<img src="img/img4.jpg" alt="Work 4">
					<img src="img/img5.jpg" alt="Work 5">
				</div>
			</section>
			<section id="js">
				<h2>JavaScript</h2>
				<button id="newtrick" style="vertical-align:middle"><span>I have a new trick</span></button>
				<div class="accordion">
					<div class="accordion-header">
						<h4>
							<svg class="accordion-symbol" viewBox="0 0 24 24">
								<path d="M10 17l5-5-5-5"></path>
							</svg> 
								Click me
						</h4>
					</div>
					<div class="accordion-content extra-style">
						<p class="center-text">Maybe I should learn Python</p>
					</div>
				</div>
			</section>
			<section id="contact">
				<h5>Contact Me</h5>
				<form>
					<label for="name">Name:</label>
					<input type="text" id="name" name="name"><br>
					<label for="email">Email:</label>
					<input type="email" id="email" name="email"><br>
					<label for="message">Message:</label>
					<textarea id="message" name="message"></textarea><br>
					<input type="submit" value="Send">
				</form>
			</section>
		</main>
		<footer>
			<p>&copy; 2023 "NoSad"</p>
		</footer>
		<script src="script1.js"></script>
		<script src="page1.js"></script>
		<script src="page3.js"></script>
		<script src="accordion.js"></script>
		<script src="alert.js"></script>
		<script src="timer.js"></script>
	</body>
</html>