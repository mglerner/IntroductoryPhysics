# IntroductoryPhysics

People have written more eloquently than I can about this (e.g Chanda Prescod-Weinstein's 
[Decolonising Science Reading
List](https://medium.com/@chanda/decolonising-science-reading-list-339fb773d51f#.3yyou2as5)
and her followup articles including [Making Meaning of "Decolonising"](https://medium.com/@chanda/making-meaning-of-decolonising-35f1b5162509)). It
is certainly true, for instance, that  working through a common
syllabus with a standard textbook will have intro students looking at
a progression of Physicists all of whom look like Newton.

As a teacher, I thought "oh, I'll just grab someone else's annotated
syllabus so that I can consistently augment my own class with a more
inclusive (note: now I might say 'decolonised' .. but I'm not sure 
I'm quite sophisticated enough in my language) set of models." I
poked around the internet, but couldn't find such a syllabus. So, as
part of my intro class, one of the assignments is essentially "find an
example of a Physicist who doesn't look like Newton, write something
about that person, include a picture if you can, and figure out where
that person could have been included in our syllabus." The assignment
gets the full weight of any other weekly assignment. I'm putting this
on github (1) so that it can be a resource for others (ideally, you'd
be able to say "oh, I'm covering Knight Chapter 3, Section 2 today
... here's a quick PPT slide I can slip in with my clicker questions")
(2) so that people can send in
[PRs](https://help.github.com/articles/about-pull-requests/) to make
this better.

Some details:

In order to make contributions easy, information about each scientist
lives in a different file. It's a simple text file, and I've set up a
page that can make one for you
[here](https://mglerner.github.io/pages/nonnewtonian-scientists.html). Check
it out!

If you like, you can also make a file directly yourself. Here is an
[Example File](ExampleScientist.txt).

* Add as much of the information as you can, but please feel
  *encouraged* to send me incomplete files if that's what you have!
  Something is way better than nothing!

* Try to follow the format as well as you can (filling in the boxes on
  the
  [form](https://mglerner.github.io/pages/nonnewtonian-scientists.html)
  makes this really easy!). If you send me files
  (either via email <mglerner@proton.com> or as a PR), I'll gladly reformat them to fix any
  small mistakes, so don't let that stop you!

* Please cite your sources (Wikipedia is OK!), and feel free to quote
  explicitly, but don't plagiarize!

* Including links to pictures really helps!

Here's the actual script/assignment I use in class:

>The content of this particular course (and this particular
textbook) has pretty much focused on ideas developed by white,
European men. In fact, working through a common syllabus with a
standard textbook will have you looking at a progression of
Physicists all of whom (to within rounding error) look like
Newton. I'd like to say that's a historical accident, but it's actually
more complicated than that, and perhaps not always so benign as the
word "accident" might imply.

>Your task in this assignment is to broaden this focus by writing a
paragraph or so about someone who's made a significant contribution
to Physics and who is not a white, European male. This can be a
contemporary or a historical figure. Try to find someone you don't
already know about - or perhaps someone you do know about but think
should be better known. Your paragraphs should include telling us
who the person is, the contribution(s), the significance of the
contribution(s), something about that person's life and how it
impacted that person's experience that led to his or her
discoveries. Next, looking through the table of contents and/or
index of your textbook, tell us where the person's contributions
might be placed in this textbook (the textbook covers a very large
amount of Physics, so you may be able to answer this part even if we
won't cover the relevant contributions this semester). Finally, if
at all possible, please include a link to a picture of the person.

>It would be great if everyone found a different scientist to
describe, so if you know whom someone else is choosing to write
about, please choose someone else.

>Our intention is to make the results of this assignment public, so
please submit your assignment in the format described by the example
file located at https://goo.gl/AkT97E and please note that it's really
easy to create your own file by using the
[form](https://mglerner.github.io/pages/nonnewtonian-scientists.html). Since
we plan to make this
public, please be sure either to include your name if you'd like
your name included in the text, or to leave it out if you don't want
it included. Please remember to cite your sources.


The python script here autogenerates annotated tables of contents. I usually 
run it via the Jupyter notebook, Annotating.ipynb.

Also worth noting: when I assign this in class as a Moodle assignment, Moodle tends to turn markdown into HTML. To get the markdown back, I use [html2text](https://github.com/Alir3z4/html2text/) (originally written by Aaron Swartz). I do this on the command line, in zsh:

```bash
for f in *.html; do html2text < $f > ${f:r}.md; done
```

TODO
* Add more textbooks
* Focus on 2nd semester
* Make everyone go through the form
* Fix mixup between calc-based and algebra-based
* Make a drop-down in the form for textbooks, or split it up into
sections like "Author, Title, Edition"
* Allow multiple textbooks. This may mean parsing the MD into an
  object. First thought on that object, it's heart is a list of lists,
  and it has a fancy getter function which can take context (need the
  raw image url for making your PPTX? Cool. Need it wrapped in an
  image tag, which is wrapped in an anchor tag? cool.)


Here's the current version, which obviously needs more scientists
added:

**CLICK on the photo for a powerpoint slide, or download the whole
  slide deck for Knight, 3rd edition (calc-based)**
  [here](Textbooks%2FKnight%2C%203rd%20edition.pptx) **!!!**

**WARNING: Some of the content got mixed up between the calc-based
  class and the algebra-based class. I need to fix it. The
  descriptions and pictures should be right, but the chapters may be wrong.**

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Photo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>Name</th>
      <th>Description</th>
      <th>Sources</th>
      <th>Contributor</th>
      <th>Contributors</th>
    </tr>
    <tr>
      <th>Chapter</th>
      <th>Section</th>
      <th>Topics</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <th></th>
      <th>Motion, Velocity, Acceleration</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <th></th>
      <th>1D Kinematics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <th></th>
      <th>Vectors</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <th></th>
      <th>2D kinematics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <th></th>
      <th>Force and Motion, Newton's 1st and 2nd laws</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">6</th>
      <th>6</th>
      <th></th>
      <td><a href="Textbooks/Ronald McNair.pptx"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/Ronald_mcnair.jpg" width="300"/></a></td>
      <td>Ronald McNair</td>
      <td>McNair was an American physicist and an astronaut for NASA. He only lived until the age of 36, for he died during the launch of the Space Shuttle Challenger in 1986. He received his bachelors from North Carolina A & T State, and received doctorates from MIT, NC A&T State, Morris College and Univ. or South Carolina. McNair was a 5th degree black belt in karate and a performing Jazz saxophonist.</td>
      <td>Biographical Data of Ronald E. McNair. (2003, December). Retrieved February 20, 2018, from<a href="https://www.jsc.nasa.gov/Bios/htmlbios/mcnair.html">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <th>Equilibrium, Mass, Weight, Gravity, Friction, Drag, motion along a line</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <th></th>
      <th>Newton's third law</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <th></th>
      <th>Dynamics in a plane</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>9</th>
      <th></th>
      <th>Impulse and momentum</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">10</th>
      <th rowspan="2" valign="top"></th>
      <th>Energy</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td><a href="Textbooks/Emmy Noether.pptx"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Noether.jpg/330px-Noether.jpg" width="300"/></a></td>
      <td>Emmy Noether</td>
      <td>Amalie Emmy Noether was a German mathematician and physicist known for her landmark contributions to abstract algebra and theoretical physics. One of her most remarkable discoveries in physics was Noether's theorem. The theorem states that every differentiable symmetry of the action of a physical system has a corresponding conservation law. In 1915, Noether was helping two other scientists, David Hilbert and Felix Klein, to understand Albert Einstein's general relativity theory when she proved Noether's first theorem. Upon receiving her work, Einstein wrote to Hilbert: "Yesterday I received from Miss Noether a very interesting paper... I'm impressed that such things can be understood in such a general way. The old guard at Göttingen should take some lessons from Miss Noether! She seems to know her stuff." Noether's theorem has become a fundamental tool of modern theoretical physics because of the insight it gives into conservation laws and also being practical calculation tool. For example, suppose that a new physical phenomenon is discovered. Noether's theorem provides a test for theoretical models of the phenomenon: if the theory has a continuous symmetry, then Noether's theorem guarantees that the theory has a conserved quantity, and for the theory to be correct, this conservation must be observable in experiments.</td>
      <td><a href="https://en.wikipedia.org/wiki/Emmy_Noether">Link1</a></td>
      <td>Mai Hoang</td>
      <td></td>
    </tr>
    <tr>
      <th>11</th>
      <th></th>
      <th>Work</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>12</th>
      <th></th>
      <th>Rotation of a rigid body</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">13</th>
      <th rowspan="3" valign="top"></th>
      <th>Newton's theory of Gravity</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Qiudong Wang</td>
      <td>Qiudong Wang, mathematical physicist, found an infinite-series solution to the generalized “n-body” problem, which is important in predicting the motions of planetary systems.</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Subrahmanyan Chandrasekhar</td>
      <td>Indian physicist, worked on wide range of astrophysical problems. Developed a theory about the structure of white dwarf stars, placed upper limit on mass of white dwarf stars.</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>14</th>
      <th></th>
      <th>Oscillations</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">15</th>
      <th rowspan="3" valign="top"></th>
      <th>Fluids and elasticity</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td><a href="Textbooks/Ruby Payne-Scott.pptx"><img src="https://csiropedia.csiro.au/wp-content/uploads/2015/01/6235943.jpg" width="300"/></a></td>
      <td>Ruby Payne-Scott</td>
      <td>Ruby Payne-Scott was an Australian born physicist and radio astronomer. She began work as a physicist with the cancer treatment center at the University of Sydney where she focused on radiation therapy as a form of cancer treatment. She later completed her master's thesis on wavelength distributions of radiation. Ruby worked briefly as a teacher before receiving a job in the radiophysics division of the Commonwealth Scientific and Industrial Research Organization where she worked on radar technology for the army. Her most notable contribution, however, lay in her interest in extraterrestrial radio signals. She demonstrated, with the help of two colleagues, that radio brightness across the sky could be treated as a two-dimensional sum of an infinite series of simple waveforms and showed that it could be computed using the Fourier transform. Ruby's work served as a mathematical foundation for radio astronomy. In addition to being a brilliant scientist, she was an avid supporter of women's rights believing in equal employment and pay for women.</td>
      <td>Goss, W., & Hooker, C. (2018). Biography - Ruby Violet Payne-Scott - Australian Dictionary of Biography. Adb.anu.edu.au. Retrieved 19 February 2018, from<a href="http://adb.anu.edu.au/biography/payne-scott-ruby-violet-15036">Link1</a>  Ruby Payne-Scott [1912-1981] - CSIROpedia. (2018). CSIROpedia. Retrieved 19 February 2018, from<a href="https://csiropedia.csiro.au/payne-scott-ruby/">Link2</a></td>
      <td></td>
      <td>Megan Hedinger</td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Garret Morgan</td>
      <td>Invented the smoke mask, which uses many mechanisms studied in physics like gas separation depending on density. He also used electricity to invent electric traffic signals in Cleveland.</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>16</th>
      <th></th>
      <th>Macroscopic description of matter</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">17</th>
      <th>4</th>
      <th></th>
      <td><a href="Textbooks/Bhāskara II.pptx"><img src="http://www.famousmathematicians.com/wp-content/uploads/2016/09/bhaskara-273x300.jpg" width="300"/></a></td>
      <td>Bhāskara II</td>
      <td>Bhāskara II was a 12th century Indian mathematician and astronomer. Among his many notable accomplishments, which include using differentials centuries before Newton “invented” calculus (Bhāskara II), Bhāskara II was one of the first to design a perpetual motion machine. The “Bhāskara wheel” has curved spokes filled with mercury, which flows downward in the direction of rotation, theoretically creating a shifting force to power perpetual rotation (Simanek 2010). Unfortunately, Bhāskara II didn’t account for the unbalancing effect of the mercury flow, which shifts the wheel’s center of mass and eventually disrupts rotation (Simanek). Bhāskara II’s design has remained a fascination for physicists and countless researchers have tried to optimize his design and create a truly perpetually rotating wheel.  All have failed (Simanek). Bhāskara II was instrumental is the development of Indian mathematics, and was honored in 1981 with an eponymous satellite (Bhāskara II).</td>
      <td>“Bhāskara II.” Wikipedia: The Free Encyclopedia. Wikimedia Foundation, Inc. 22 July 2004. Web. Accessed 30 Sept. 2017.<a href="https://en.wikipedia.org/wiki/Bh%C4%81skara_II#Engineering">Link1</a>  Simanek, Donald. 2010. “The Shifting-Mass Overbalanced Wheel.” The Museum of Unworkable Devices, Lock Haven University. Accessed 30 Sept. 2017.<a href="http://www.lhup.edu/~dsimanek/museum/overbal.htm">Link2</a></td>
      <td></td>
      <td>Jacob Harris</td>
    </tr>
    <tr>
      <th></th>
      <th>Work, heat, 1st law of thermodynamics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>18</th>
      <th></th>
      <th>Micro/macro connection for gas/thermo, entropy, 2nd law</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">19</th>
      <th rowspan="2" valign="top"></th>
      <th>Heat engines and refrigerators</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td><a href="Textbooks/Arthur Walker Jr..pptx"><img src="http://www.math.buffalo.edu/mad/PIX/Walker.abc_old.jpg" width="300"/></a></td>
      <td>Arthur Walker Jr.</td>
      <td>Arthur Bertram Cuthbert Walker Jr. (1936-2001) was a solar physicist and a pioneer of EUV/XUV. He was born in Cleveland, Ohio. Dr. Walker Jr. completed his undergraduate studies at Case Institute of technology in Cleveland in 1957 and earned his bachelor’s degree in physics. He completed both his master’s and doctorate degrees in astrophysics in the University of Illinois, in 1958 and 1962 respectively. He is most noted for having developed the solar corona. Two of his sounding rocket payloads, the Stanford/MSFC Rocket Spectroheliograph Experiment and the Multi-Spectral Solar Telescope Array, recorded the first full-disk, high-resolution images of the Sun in XUV with conventional geometries of normal incidence optics; this technology is now used in solar telescopes such as SOHO/EIT and TRACE, and in the fabrication of microchips via ultraviolet photolithography. Dr. Walker's scientific research focused on radiation from the Sun called extreme ultraviolet light and soft X-rays, which affect the chemistry of Earth's upper atmosphere, including the ozone layer. In the late 1970's, Dr. Walker became interested in what was then considered a risky and untested concept, called multilayer technology, for making special telescope mirrors that could reflect that radiation. He was a professor at Stanford University from 1974 until his death in 2001 and was a member of the Stanford’s Center for Space and Astrophysics at the school. In addition to his impressive contributions to the field, Dr. Walker Jr. spent a lifetime helping women and minority students find careers in science. He is credited with helping Stanford produce more black physicists with Ph.D.’s than any other university in the nation.</td>
      <td>Arthur Bertram Cuthbert Walker, Jr. (n.d.). Retrieved February 18, 2018, from<a href="http://www.math.buffalo.edu/mad/physics/walker_arthurbc.html">Link1</a>  Arthur Bertram Cuthbert Walker, Jr. (n.d.). Retrieved February 18, 2018, from<a href="http://www.math.buffalo.edu/mad/physics/walker_arthurbc.html">Link2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>20</th>
      <th></th>
      <th>Traveling Waves</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>21</th>
      <th></th>
      <th>Superposition</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">22</th>
      <th>1</th>
      <th></th>
      <td><a href="Textbooks/Shirley Ann Jackson.pptx"><img src="https://cdn-blog.adafruit.com/uploads/2015/02/Shirley-Ann-Jackson.jpg" width="300"/></a><a href="Textbooks/Shirley Ann Jackson.pptx"><img src="https://thenotesofe.files.wordpress.com/2015/03/jackson_8x10.jpg" width="300"/></a></td>
      <td>Shirley Ann Jackson</td>
      <td>Shirley Ann Jackson is an African-American physicist born in Washington D.C., on August 5th, 1946. She was the first African American women to get a PhD from MIT. Dr.Jackson studied hadrons as a research associate at the Fermi National Accelerator Laboratory in Batavia, Illinois. She was also a visiting scientist at CERN in Switzerland where she worked on theories relating to elementary particles. She was a part of the Theoretical Physics Research Department at AT&T Bell Laboratories in 1976 and studied materials used in the semiconductor industry. She also researched on the optical and electronic properties of two-dimensional and quasi-two dimensional systems. She made contributions to the knowledge of charged density waves in layered compounds and optical and electronic properties of semiconductor strained-layer superlattices. Since her postgraduate studies, she has been active in initiatives to increase African American participation in science and math. She has been serving as the president of Rensselear Polytechnic Institute since July 1, 1999. She was the first black woman to earn a PhD from MIT. She was the first black woman to be elected to the National Academy of Engineering. She did most of her research on optical and electronic properties of layered materials, surface electrons of liquid helium films, strained-layer semiconductor superlattices, and most notably, the polaronic aspects of electrons in two- dimensional systems.</td>
      <td>[https://en.wikipedia.org/wiki/Shirley_Ann_Jackson](https://en.wikipedia.org/wiki/Shirley_Ann_Jackson) [http://www.nytimes.com/ref/college/faculty/coll_pres_jacksonbio.html](http://www.nytimes.com/ref/college/faculty/coll_pres_jacksonbio.html) [Diaz, S. (n.d.). Jackson, Shirley Ann.](http://www.blackpast.org/aah/jackson-shirley-ann-1946)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <th>Wave Optics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>23</th>
      <th></th>
      <th>Ray Optics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>24</th>
      <th></th>
      <th>Optical Instruments</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>25</th>
      <th></th>
      <th>Electric Charges and Forces</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>26</th>
      <th></th>
      <th>The Electric Field</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>27</th>
      <th></th>
      <th>Gauss’s Law</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">28</th>
      <th rowspan="2" valign="top"></th>
      <th>The Electric Potential</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td><a href="Textbooks/Michio Katu.pptx"><img src="https://innotechtoday.com/wp-content/uploads/2017/03/Micio-new-2.jpg" width="300"/></a></td>
      <td>Michio Katu</td>
      <td>Professor Michio Kaku, born in 1947, is a theoretical physicist, futurist, and popularizer of science. He is one of the co-founder of string field theory, a branch of string theory, which intends to unite Albert Einstein's earlier findings with quantum physics. His research focuses on superstring theory, supergravity, supersymmetry, and hadronic physics. He has authored more than 70 articles and several highly-accessible science books. He grew up a science enthusiast. Story has it that he built an atom smasher in his parents' garage for his high school science fair. His effort to popularize science has made him a well-known public figure. He has made multiple appearance on TV programs and film. A fun fact about him is that in 2016, he appeared in a TV commercial for Turbo Tax. He has spent majority of his academic career teaching Theorectical Physics at the City College of New York.</td>
      <td>Michio Kaku Biolography (April 2,2014) Retrived from <https://www.biography.com/people/michio-kaku-21429817> access date February 18, 2018)</td>
      <td></td>
      <td>Yuyu Zhang</td>
    </tr>
    <tr>
      <th>29</th>
      <th></th>
      <th>Potential and Field</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">30</th>
      <th>3</th>
      <th></th>
      <td><a href="Textbooks/Shin'ichirō Tomonaga.pptx"><img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/Tomonaga.jpg" width="300"/></a></td>
      <td>Shin'ichirō Tomonaga</td>
      <td>Shin'ichirō Tomonaga was born on March 31, 1906 in Tokyo, Japan. He is a Japanese scientist who won the Nobel Prize in Physics in 1965 for developing basic principles of quantum electrodynamics. He was a professor of Physics at the Tokyo University of Education. From 1937 to 1939, he was in Germany to study nuclear physics and the quantum field theory. In 1940, he developed the intermediate coupling theory in order to clarify the structure of the meson cloud around the nucleon. During WWII, he solved the motion of electrons in the magnetron and also developed a unified theory of systems consisting of wave guides and cavity resonators. Dr. Tomonaga was the President of the Tokyo University of Education from 1956 to 1962. He has actively campaigned against the spread of nuclear weapons and for peaceful use of nuclear energy.</td>
      <td><a href="https://www.britannica.com/biography/Tomonaga-Shinichiro">Link1</a> <a href="https://www.nobelprize.org/nobel_prizes/physics/laureates/1965/tomonaga-">Link2</a>  bio.html<a href="https://en.wikipedia.org/wiki/Shin%27ichir%C5%8D_Tomonaga">Link3</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <th></th>
      <td><a href="Textbooks/Warren Henry.pptx"><img src="http://www.math.buffalo.edu/mad/PIX/henry_warren.howard1.jpg" width="300"/></a></td>
      <td>Warren Henry</td>
      <td>Warren Henry was an African American Physicist that had somewhat of an astute background for a black man of his time. Both of his parents had graduated from the Tuskegee Institute, and George Washington Carver lived and conducted research on his parent’s farm during the summer months (Williams). It can be quite apparent to see where his interest in the sciences more than likely came from during his childhood. He later attended Tuskegee where he majored in Mathematics, English, and French (Williams). Later wanting to conduct research, he turned to Rutgers University where they then turned him away (Williams).  As a result, he ended up going to the Naval Research Laboratory where he would reside for the next 12 years (Williams). During that time he was able to research and gain the knowledge of materials that were at a rather low temperature (Williams). His expertise regarding low-temperature research was probably unsurpassed in the U.S. while at the Naval Research Laboratory. He was also the head of several projects at several institutions like UC Berkeley amongst others. Even though his research in low temperatures was quite significant, he was most known for his work in magnetism and superconductivity. His work in this field was what brought him the most praise by the scientific community. He had written a highly detailed study that consisted of a "demonstration of the proof of non-interacting paramagnetic ions and how they’re a significant contribution” when considering magnetism and superconductivity (Williams). His work was a significant contribution to the world because his models and ideas have been implemented into modern textbooks, and are still widely used to this day. A prime example of that being the demonstration I had spoken of earlier that took place back in 1934. In relation to where Henry’s work can be found in the textbook, I would imagine that his material could be found in chapter 32 and 33 where it talks about the magnetic field of a current and electromagnetic induction.</td>
      <td>Physics Central. “Africn Americans in Physics.” Physics Buzz, American Physical Society, 27 Feb. 2013,<a href="http://physicsbuzz.physicscentral.com/2013/02/african-americans-in-">Link1</a>  physics.html Williams, Scott. “Physicist of the African Diaspora - Warren E Henry.” Warren E. Henry - Physicist of the African Diaspora, Bonvibre & Daughters,<a href="http://www.math.buffalo.edu/">Link2</a>  mad/physics/henry_warren.html</td>
      <td></td>
      <td>Joshua Maclin</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top"></th>
      <th>Current and Resistance</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td><a href="Textbooks/Isamu Akasaki.pptx"><img src="http://ethw.org/w/images/7/7c/Isamu_Akasaki_2482.jpg" width="300"/></a></td>
      <td>Isamu Akasaki</td>
      <td>The main contribution of Isamu Akasaki is in the semiconductor field. He, along with Hiroshi Amano and Shuji Nakamura invented efficient blue light-emitting diodes, and won the 2014 Noble Prize in Physics. He worked on GaN to make high-brightness blue LED light. As a result, people are able to have bright white LED light as an energy-saving light source.</td>
      <td>"Isamu Akasaki." Isamu Akasaki - Engineering and Technology History Wiki,<a href="http://ethw.org/Isamu_Akasaki">Link1</a>  "Isamu Akasaki." Wikipedia, Wikimedia Foundation, 4 Oct. 2017,<a href="http://en.wikipedia.org/wiki/Isamu_Akasaki">Link2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>31</th>
      <th></th>
      <th>Fundamentals of Circuits</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">32</th>
      <th>2</th>
      <th></th>
      <td><a href="Textbooks/Margaret Murnane.pptx"><img src="https://jila.colorado.edu/kmlabs/sites/default/files/styles/200_image/public/images/bios/Margaret_Murnane_portrait.jpg?itok=jY-_AF2Q" width="300"/></a></td>
      <td>Margaret Murnane</td>
      <td>Margaret Murnane is an optical physicist at the University of Colorado. She has built "the fastest things that humans have ever created" lasers which can flash for "ten quadrillionths of a second"! Her background includes the fact that "physics was [her] worst subject in high school" but she dreamed of being a physicist because she loved the "excitement of discovery." She and her husband now run a lab at the University of Colorado. In the lab, she records "some of the fastest motions in our natural world." Her lasers can capture the movement of electrons. Her newest laser and x-ray beams can flash for less than 0.00000000000000001 seconds. Talk about "in the blink of an eye!" She is able to pass on excitement and knowledge to students. Scientists use her lasers which are based on her titanium-sapphire design to study a wide range of phenomena (chemical reactions, etc.).</td>
      <td><a href="https://en.wikipedia.org/wiki/Margaret_Murnane">Link1</a> <a href="https://jila.colorado.edu/kmlabs/bio/murnane">Link2</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <th>The Magnetic Field</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>33</th>
      <th></th>
      <th>Electromagnetic Induction</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>34</th>
      <th></th>
      <th>Electromagnetic Fields and Waves</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>35</th>
      <th></th>
      <th>AC Circuits</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>36</th>
      <th></th>
      <th>Relativity</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>37</th>
      <th></th>
      <th>The Foundations of Modern Physics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>38</th>
      <th></th>
      <th>Quantization</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>39</th>
      <th></th>
      <th>Wave Functions and Uncertainty</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">40</th>
      <th rowspan="3" valign="top"></th>
      <th>One-Dimensional Quantum Mechanics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Sandra Faber</td>
      <td>Sandra Moore Faber (born December 28, 1944) is a University Professor of Astronomy and Astrophysics at the University of California, Santa Cruz, and works at the Lick Observatory. She has made important discoveries linking the brightness of galaxies to the speed of stars within them and was the co-discoverer of the Faber–Jackson relation. Faber was also instrumental in designing the Keck telescopes in Hawaii. Faber studied at Swarthmore College, majoring in Physics and minoring in Mathematics and Astronomy. She earned her B.A. in 1966. Soon after she went on to earn her Ph.D. at Harvard University in 1972, where she studied Optical Observational Astronomy. During this time the only observatory open to her was the Kitt Peak National Observatory, which had inadequate technology for the complexity of her thesis. She is a woman.</td>
      <td><a href="https://en.wikipedia.org/wiki/Sandra_Faber">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Lene Hau</td>
      <td>Lene Vestergaard Hau (born November 13, 1959 in Vejle, Denmark) is a Danish physicist. In 1999, she led a Harvard University team who, by use of a Bose-Einstein condensate, succeeded in slowing a beam of light to about 17 metres per second, and, in 2001, was able to stop a beam completely. Later work based on these experiments led to the transfer of light to matter, then from matter back into light,[2] a process with important implications for quantum encryption and quantum computing. More recent work has involved research into novel interactions between ultracold atom and nanoscopic scale systems. In addition to teaching physics and applied physics, she has taught Energy Science at Harvard,[3] involving photovoltaic cells, nuclear power, batteries, and photosynthesis</td>
      <td><a href="https://en.wikipedia.org/wiki/Lene_Hau">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>41</th>
      <th></th>
      <th>Atomic Physics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">42</th>
      <th rowspan="2" valign="top">2</th>
      <th></th>
      <td><a href="Textbooks/Tsung-Dao Lee.pptx"><img src="https://upload.wikimedia.org/wikipedia/commons/5/53/TD_Lee.jpg" width="300"/></a></td>
      <td>Tsung-Dao Lee</td>
      <td>Tsung-Dao Lee is a Chinese-American physicist, known for his work on parity violation, the Lee Model, particle physics, relativistic heavy ion physics, nontopological solitons and soliton stars. He was a recipient of the 1957 Nobel Prize in Physics at the age of 30. Lee conducted the majority of his life's research at Columbia University, where his first work was on a solvable model of quantum field theory known as the Lee Model. Later, he worked on the puzzle of K meson decay, through which he studied parity non-conservation in weak interactions. This work led to his winning the Nobel Prize in Physics. He was also very active in statistical mechanics, astrophysics, and a number of other disciplines.</td>
      <td>Lee, T. D., & Yang, C. N. (1956). Question of parity conservation in weak interactions. Physical Review, 104(1), 254. Lee, T. D. (1981). Particle Physics and Introduction to Field Theory, Comtemporary Concepts in Physics Vol. 1. Harwood academic publishers. Lee, T. D., & Yang, C. N. (1952). Statistical theory of equations of state and phase transitions. II. Lattice gas and Ising model. Physical Review, 87(3), 410. Yang, C. N., & Lee, T. D. (1952). Statistical theory of equations of state and phase transitions. I. Theory of condensation. Physical Review, 87(3), 404.</td>
      <td></td>
      <td>Khai Nguyen</td>
    </tr>
    <tr>
      <th></th>
      <td><a href="Textbooks/Chien-Shiung Wu.pptx"><img src="http://www.history.com/images/media/slideshow/women-in-science-and-health/chien-shiung-wu.jpg" width="300"/></a></td>
      <td>Chien-Shiung Wu</td>
      <td>Chien-Shiung Wu (1912-1997) was a Chinese-American experimental physicist who made significant contributions in the field of nuclear physics1 (Wikipedia). Wu worked on the infamous Manhattan Project where she developed the process of separating uranium metal to uranium-235 and uranium-238 by gaseous diffusion1 (Wikipedia). Her work was credited to contradict the hypothetical Law of Conservation of Parity, which at the time was a well-established law and basically entailed a very complicated way of proving the idea of symmetry, where particles that are mirror images of each other will act in identical ways3 (ListVerse). Her experiments were incredibly significant in that she was able to show that one particle was more likely to eject an electron than the other and they were therefore not symmetrical and that observation overturned a 30-year belief and shattered the conservation of parity law3 (ListVerse). The discovery of parity violation was a major contribution to particle physics and the development of the Standard Model which is a paradigm of the modern quantum field theory2 (Wikipedia). It is little wonder that Wu is now hailed as “The First Lady of Physics” and the “Chinese Marie Curie”1(Wikipedia). However, unfortunately, like many of her contemporary female scientists, Wu’s work was discredited and her male co-workers Lee and Yang got awarded the Nobel Prize for Physics for ‘her’ experiment3 (ListVerse). In fact, she received no mention or credit for her significant contribution to the project until 1978, when she was awarded the inaugural Wolf Prize for Physics two decades after her ground-breaking experiment1(Wikipedia).</td>
      <td>Chien-Shiung Wu. Wikipedia. The Free Encyclopedia. Wikimedia Foundation, Inc. 20 September 2017. Web. 06 October 2017.<a href="https://en.wikipedia.org/wiki/Chien-Shiung_Wu">Link1</a>  Standard Model. Wikipedia. The Free Encyclopedia. Wikimedia Foundation, Inc. 16 September 2017. Web. 06 October 2017.<a href="https://en.wikipedia.org/wiki/Standard_Model">Link2</a>  10 Groundbreaking Women Scientists Written Off By History. Shelby Hoebee. October 14, 2013. ListVerse.<a href="http://listverse.com/2013/10/14/10-groundbreaking-women-scientists-written-off-by-history/">Link3</a>  Accessed 06 October 2017.</td>
      <td></td>
      <td>Khyrul Khan</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top"></th>
      <th>Nuclear Physics</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Ursula Franklin</td>
      <td>Ursula Martius Franklin, CC OOnt FRSC (16 September 1921 – 22 July 2016), was a German-Canadian metallurgist, research physicist, author, and educator who taught at the University of Toronto for more than 40 years. Franklin was a pioneer in the field of archaeometry, which applies modern materials analysis to archaeology. She worked for example, on the dating of prehistoric bronze, copper and ceramic artifacts. In the early 1960s Franklin was one of a number of scientists who participated in the Baby Tooth Survey, a project founded by Eric and Louise Reiss along with other scientists such as Barry Commoner, which investigated levels of strontium-90—a radioactive isotope in fallout from nuclear weapons testing—in children's teeth. This research contributed to the cessation of atmospheric weapons testing. Franklin published more than a hundred scientific papers and contributions to books on the structure and properties of metals and alloys as well as on the history and social effects of technology.</td>
      <td><a href="https://en.wikipedia.org/wiki/Ursula_Franklin#Scientific_research">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Lise Meitner</td>
      <td>Lise Meitner (English /ˈliːzə ˈmaɪtnər/; 7 November 1878 – 27 October 1968) was an Austrian-Swedish physicist who worked on radioactivity and nuclear physics. Otto Hahn and Meitner led the small group of scientists who first discovered nuclear fission of uranium when it absorbed an extra neutron; the results were published in early 1939. Meitner and Otto Frisch understood that the fission process, which splits the atomic nucleus of uranium into two smaller nuclei, must be accompanied by an enormous release of energy. This process is the basis of the nuclear weapons that were developed in the U.S. during World War II and used against Japan in 1945. Nuclear fission is also the process exploited by nuclear reactors to generate electricity.</td>
      <td><a href="https://en.wikipedia.org/wiki/Lise_Meitner">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td>Fabiola Gianotti</td>
      <td>Fabiola Gianotti (born October 29, 1960) is an Italian particle physicist, currently CERN (European Organization for Nuclear Research) Director-General and the first woman to hold this position. Fabiola Gianotti received a Ph.D. in experimental particle physics from the University of Milan in 1989. Since 1996, following several postdoctoral positions, including a fellowship at CERN, she has been a research physicist in the Physics Department of CERN, the European Organization for Nuclear Research, and since August 2013 an honorary Professor at the University of Edinburgh. She is also a member of the Italian Academy of Sciences (Accademia Nazionale dei Lincei), foreign associate member of the US National Academy of Sciences[4] and foreign associate of the French Academy of Science. Gianotti has worked on several CERN experiments (WA70, UA2 experiment, ALEPH, ATLAS), being involved in detector R&D and construction, software development and data analysis.</td>
      <td><a href="https://en.wikipedia.org/wiki/Fabiola_Gianotti">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

And here are some scientists descriptions my students wrote up. Feel
free to add them!

# Scientists

## En'hedu'anna

Somebody needs to include her! The first scientist we have a record of
a is a Sumerian woman astronomer! Here are
[some](http://womeninastronomy.blogspot.com/2013/05/enheduanna-our-first-great-scientist.html)
[pointers](https://en.wikipedia.org/wiki/Enheduanna) to start!

## Zhang Heng

Zhang Heng, astronomer, mathematician, inventor and poet in China’s
Han Dynasty (78-139 C.E.).  Invented the world’s first seismometer
(for detecting earthquakes), improved the water clock, and developed a
water-powered instrument to help measure the positions of stars and
planets.

## Henrietta Swan Leavitt

Henrietta Swan Leavitt, whose job was documenting the characteristics
of "Cephid variable" stars in the early 1900’s, before computers were
available to do such work.  These stars have a brightness that varies
with a stable period, and Henrietta’s job was to look at photographic
plates that contained images such variable stars. In the process of
examining over 1700 images of stars in a nearby galaxy, she discovered
an important regularity between the brightness of such stars and the
period of the variation of the star.  That discovery let scientists
determine the distance to other galaxies, which helped lead to the
discovery that the universe is expanding.

## Whisoh Lee

Whisoh Lee, a Korean theoretical physicist worked on fundamental
particle physics, and whose work influenced Abdus Salam’s work on
electro-weak theory as well as the developing the basis for the Higg’s
mechanism.

## Abdus Salam

Abdus Salam– Pakistani theoretical physicist, earned the Nobel Prize
in 1979 for his work unifying electromagnetism with the weak
interaction (responsible for "beta decay" of radioactive elements).

## Ibn Sahl

Snell's law was "first discovered in the 10th century by the Persian scientist Ibn Sahl, not centuries later by Snell" [Scientists Must Challenge What Makes Studies Scientific](https://www.americanscientist.org/blog/macroscope/scientists-must-challenge-what-makes-studies-scientific)

## Al Hazen Ibn al-Haytham

Invented pinhole camera [Wikipedia entry](https://en.wikipedia.org/wiki/Ibn_al-Haytham)
