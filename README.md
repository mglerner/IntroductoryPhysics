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
inclusive (note: now I might say 'decolonised') set of models." I
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
lives in a different file. Here is an
[Example File](ExampleScientist.txt).

* Add as much of the information as you can, but please feel
  *encouraged* to send me incomplete files if that's what you have!
  Something is way better than nothing!

* Try to follow the format as well as you can. If you send me files
  (either via email <mglerner@gmail.com> or as a PR), I'll gladly reformat them to fix any
  small mistakes, so don't let that stop you!

* Please cite your sources (Wikipedia is OK!), and feel free to quote
  explicitly, but don't plagiarize!

* Including links to pictures really helps!

The python script here autogenerates annotated tables of contents!
Here's the current version, which obviously needs more scientists
added:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Name</th>
      <th>Photo</th>
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
      <th>6</th>
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
      <th>10</th>
      <th></th>
      <th>Energy</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
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
      <td>Qiudong Wang</td>
      <td></td>
      <td>Qiudong Wang, mathematical physicist, found an infinite-series solution to the generalized “n-body” problem, which is important in predicting the motions of planetary systems.</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>Subrahmanyan Chandrasekhar</td>
      <td></td>
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
      <th rowspan="2" valign="top">15</th>
      <th rowspan="2" valign="top"></th>
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
      <td>Garret Morgan</td>
      <td></td>
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
      <th>17</th>
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
      <th>19</th>
      <th></th>
      <th>Heat engines and refrigerators</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
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
      <th>22</th>
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
      <th>28</th>
      <th></th>
      <th>The Electric Potential</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
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
      <th>30</th>
      <th></th>
      <th>Current and Resistance</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
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
      <td>Margaret Murnane</td>
      <td><img src="https://jila.colorado.edu/kmlabs/sites/default/files/styles/200_image/public/images/bios/Margaret_Murnane_portrait.jpg?itok=jY-_AF2Q"></td>
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
      <td>Sandra Faber</td>
      <td></td>
      <td>Sandra Moore Faber (born December 28, 1944) is a University Professor of Astronomy and Astrophysics at the University of California, Santa Cruz, and works at the Lick Observatory. She has made important discoveries linking the brightness of galaxies to the speed of stars within them and was the co-discoverer of the Faber–Jackson relation. Faber was also instrumental in designing the Keck telescopes in Hawaii. Faber studied at Swarthmore College, majoring in Physics and minoring in Mathematics and Astronomy. She earned her B.A. in 1966. Soon after she went on to earn her Ph.D. at Harvard University in 1972, where she studied Optical Observational Astronomy. During this time the only observatory open to her was the Kitt Peak National Observatory, which had inadequate technology for the complexity of her thesis. She is a woman.</td>
      <td><a href="https://en.wikipedia.org/wiki/Sandra_Faber">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>Lene Hau</td>
      <td></td>
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
      <th rowspan="4" valign="top">42</th>
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
      <td>Ursula Franklin</td>
      <td></td>
      <td>Ursula Martius Franklin, CC OOnt FRSC (16 September 1921 – 22 July 2016), was a German-Canadian metallurgist, research physicist, author, and educator who taught at the University of Toronto for more than 40 years. Franklin was a pioneer in the field of archaeometry, which applies modern materials analysis to archaeology. She worked for example, on the dating of prehistoric bronze, copper and ceramic artifacts. In the early 1960s Franklin was one of a number of scientists who participated in the Baby Tooth Survey, a project founded by Eric and Louise Reiss along with other scientists such as Barry Commoner, which investigated levels of strontium-90—a radioactive isotope in fallout from nuclear weapons testing—in children's teeth. This research contributed to the cessation of atmospheric weapons testing. Franklin published more than a hundred scientific papers and contributions to books on the structure and properties of metals and alloys as well as on the history and social effects of technology.</td>
      <td><a href="https://en.wikipedia.org/wiki/Ursula_Franklin#Scientific_research">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>Lise Meitner</td>
      <td></td>
      <td>Lise Meitner (English /ˈliːzə ˈmaɪtnər/; 7 November 1878 – 27 October 1968) was an Austrian-Swedish physicist who worked on radioactivity and nuclear physics. Otto Hahn and Meitner led the small group of scientists who first discovered nuclear fission of uranium when it absorbed an extra neutron; the results were published in early 1939. Meitner and Otto Frisch understood that the fission process, which splits the atomic nucleus of uranium into two smaller nuclei, must be accompanied by an enormous release of energy. This process is the basis of the nuclear weapons that were developed in the U.S. during World War II and used against Japan in 1945. Nuclear fission is also the process exploited by nuclear reactors to generate electricity.</td>
      <td><a href="https://en.wikipedia.org/wiki/Lise_Meitner">Link1</a></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>Fabiola Gianotti</td>
      <td></td>
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

## Dr. Sandra Faber

Dr. Sandra Faber, an astronomer who (along with Dr. Robert Jackson)
develop the Faber-Jackson relation, which established a relation
between the brightness of stars in a galaxy and that galaxy’s distance
from earth.  This relation takes into account the "tilt"" of the galaxy
with respect to the line of sight from the earth to that galaxy.  She
also designed the Keck observatory on Mauna Kea, a mountain in Hawaii.

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


## Emmy Noether

Why did nobody pick her yet?

## Abdus Salam

Abdus Salam– Pakistani theoretical physicist, earned the Nobel Prize
in 1979 for his work unifying electromagnetism with the weak
interaction (responsible for "beta decay" of radioactive elements).

## Chen-Ning Yang

Chen-Ning Yang, theoretical Physicist.  Born in China and educated
there and in Chicago, he and collaborator Tsung-dao Lee laid the
theoretical foundation for a model that predicted that the supposed
"conservation of Parity" law is violated in nuclear beta decay, an
important step toward the development of the "standard model" for
particle physics.  He and Lee shared the Nobel Prize in 1957.


## Chien-Shiun Wu

Chien-Shiun Wu, experimental Physicist.  Born in China and educated at
Nanking University and UC Berkeley, she helped develop the process of
separating Uranium into its two isotope (235 and 238), only one of
which (235) can be used in nuclear fission.  She later became an
expert in beta decay.  Yang and Lee asked her to study the radioactive
decay of Co-60, and her results verified the "Yang-Lee" theory, thus
disproving the supposed "conservation of Parity" in beta decay.

## Ibn Sahl

Snell's law was "first discovered in the 10th century by the Persian scientist Ibn Sahl, not centuries later by Snell" [Scientists Must Challenge What Makes Studies Scientific](https://www.americanscientist.org/blog/macroscope/scientists-must-challenge-what-makes-studies-scientific)

## Al Hazen Ibn al-Haytham

Invented pinhole camera [Wikipedia entry](https://en.wikipedia.org/wiki/Ibn_al-Haytham)
