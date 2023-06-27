<!DOCTYPE html>
<html>
	<head>
		<title>Menu</title>
			<link rel="stylesheet" href="style.css">
			<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
			<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
	</head>
	<body>
		<header>
			<h1>"NoSad" Menu <div id="right" title="This phrase will be on the right side of the page."><p> &copy </p></div></h1>
			<nav>
				<ul>
					<li><a href="#pages">Pages</a></li>
					<li><a href="#menu">Menu</a></li>
					<li><a href="#work">Work</a></li>
					<li><a href="#js">JavaScript</a></li>
				</ul>
			</nav>
		</header>
		<main>
			<button id="npage1" class="phome">Home</button>
			<section id="pages">
				<h2>Pages</h2>
				<!-- Для открытия в новой вкладке target="_blank" -->
				<p class="center-text"> This can be attributed to a link in the text to your resource -<a href="../secondpage/index.php">Just Second Page</a></p>
				<button id="npage3" class="dispage3">Button Third Page</button>
				<p class="center-text">
					<div class="page-number"><span>3</span></div> <!-- page number -->
					- Current page
				</p>
			</section> 
			<section id="menu">
				<h2>Restaurant menu</h2>
					<div class="menu-item">
						<img src="img/food1.jpg" alt="Menu Item 1">
						<div class="item-details">
							<h6 class="item-name">Pizza Mix</h6>
							<span class="item-price">$7.99</span>
							<p class="item-description">Four favorite pizzas in one: Pepperoni, Barbecue Chicken, Four Cheeses, Margaritas</p>
						</div>
					</div>
					<div class="menu-item">
						<img src="img/food2.jpg" alt="Menu Item 1">
						<div class="item-details">
							<h6 class="item-name">Burger</h6>
							<span class="item-price">$2.99</span>
							<p class="item-description">Ground turkey cutlet, burger bun, lettuce, fresh tomato, pickled cucumber, specialty cheese sauce, red sauce, red onion, cheese</p>
						</div>
					</div>
					<div class="menu-item">
						<img src="img/food3.jpg" alt="Menu Item 1">
						<div class="item-details">
							<h6 class="item-name">Sushi</h6>
							<span class="item-price">$8.99</span>
							<p class="item-description">Shanghai, Cassi, Atlantis, Thai, Tori, Nihongo</p>
						</div>
					</div>
					<div class="menu-item">
						<img src="img/food4.jpg" alt="Menu Item 1">
						<div class="item-details">
							<h6 class="item-name">Tom Yum</h6>
							<span class="item-price">$3.99</span>
							<p class="item-description">Spicy Tom Yum broth, coconut milk, galangal, lemongrass, fresh mushrooms, tomatoes, rice, choice of fillings.</p>
						</div>
					</div>
					<div class="menu-item">
						<img src="img/food5.jpg" alt="Menu Item 1">
						<div class="item-details">
							<h6 class="item-name">Wok</h6>
							<span class="item-price">$10.99</span>
							<p class="item-description">Buckwheat soba noodles, seafood, vegetable mix, teriyaki sauce.</p>
						</div>
					</div>
					<div class="menu-item">
						<img src="img/food6.jpg" alt="Menu Item 1">
						<div class="item-details">
							<h6 class="item-name">Shawarma Barbecue Large</h6>
							<span class="item-price">$2.49</span>
							<p class="item-description">Tortilla, garlic sauce, chicken, Chinese cabbage, tomato, pickled cucumber, caramelized onions, BBQ sauce.</p>
						</div>
					</div>

			</section>
			<section id="work">
				<h2>My Work</h2>
				<div class="gallery">
					<img src="img/img4.jpg" alt="Work 1">
					<img src="img/img5.jpg" alt="Work 2">
					<img src="img/img1.jpg" alt="Work 3">
					<img src="img/img2.jpg" alt="Work 4">
					<img src="img/img3.jpg" alt="Work 5">
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
		</main>
		<footer>
			<p>&copy; 2023 "NoSad"</p>
		</footer>
		<script src="script1.js"></script>
		<script src="page1.js"></script>
		<script src="page3.js"></script>
		<script src="accordion.js"></script>
		<script src="alert.js"></script>
	</body>
</html>