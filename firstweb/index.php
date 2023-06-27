<!DOCTYPE html>
<html>
  <head>
    <title>Portfolio</title>  
    <link rel="stylesheet" href="style.css">
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <style>
	body {
		font-family: 'Roboto', sans-serif;
	}
     /* Date of first code develop this website 17:10 11.05.2023 */
    </style>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
   </head>
  <body>
    <header>
      <h1>"NoSad" Portfolio <div id="right" title="This phrase will be on the right side of the page.">
       <p>&copy</p>
        </div>                                                                                  
      </h1>
      <nav>
        <ul>
          <li><a href="#disclaimer">Disclaimer</a></li>
		  <li><a href="#pages">Pages</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#work">Work</a></li>
		  <li><a href="#js">JavaScript</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
    <main>
			
		<section id="disclaimer">
			<h3>Disclaimer</h3>
			<p class="centered">
				It's part of my life, even part of my #blog. This project was created purely for entertainment and educational purposes. 
				Anything you see below is fiction.
				This project, 98% written with the help of neural networks - ChatGpt, DeepL, MidJourney<br>
				&copy"NoSad"
			</p>
		</section>
		<section id="pages">
			<h2>Pages</h2>
			<!-- Для открытия в новой вкладке target="_blank" -->
			<p class="center-text"> This can be attributed to a link in the text to your resource -<a href="secondpage/index.php">Just Second Page</a></p>
			<button id="npage3" class="npage3">Button Third Page</button>
			<p class="center-text">
				<div class="page-number"><span>1</span></div> <!-- page number -->
				- Current page
			</p>
		</section>
		<section id="about">
			<h2>About Me</h2>
			<p class="indent">
				Hi, my name is Daniel and I'm a web developer based in Thailand. I'm 22 years old, fluent in English, and can learn neural networks quickly. I'm currently learning PHP programming language, but I'm also interested in Python.
				Before diving into web development, I worked in affiliate marketing, which gave me a solid foundation in HTML. As I continued to explore the world of IT, I became fascinated with the power of neural networks and their potential applications. I spent countless hours studying and practicing to become proficient in their development.
				I'm very active on social media, using it to connect with other developers and showcase my work. You can find me on Instagram (www.instagram.com/moldavskiy8), where I share my coding journey, and on Telegram (@Sad_Manners), where I discuss the latest trends in the IT industry with other like-minded people. I also have a Vkontakte account (https://vk.com/fckeekcf), where I share my coding projects and interact with other developers, and a TikTok account (https://www.tiktok.com/@superpon4iktv), where I post fun videos that showcase my coding skills.
				As I continue to progress in the IT world, I plan to expand my portfolio to showcase my skills and expertise. So far, I've created several websites using HTML and CSS. I'm particularly excited about my experiments with Python and the potential it holds for my future projects.
				My portfolio is a testament to my passion and dedication to web development. Every project I take on helps me improve my skills and become a better web developer. I'm excited about the possibilities that lie ahead, and I can't wait to see where this journey takes me.
			</p>
		</section>
		<section id="work">
			<h2>My Work</h2>
			<div class="gallery">
			<img src="img/work1.jpg" alt="Work 1">
			<img src="img/work2.jpg" alt="Work 2">
			<img src="img/work3.jpg" alt="Work 3">
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
      <p>&copy; 2023 "NoSad" Portfolio</p>
    </footer>
    <script src="script1.js"></script>
	<script src="page3.js"></script>
	<script src="alert.js"></script>
	<script src="accordion.js"></script>
	<script src="parser.js"></script>
  </body>
</html>
