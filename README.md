# IntroductoryPhysics

People have written more eloquently than I can about this (e.g Chanda Prescod-Weinstein's 
[Decolonising Science Reading
List](https://medium.com/@chanda/decolonising-science-reading-list-339fb773d51f#.3yyou2as5)). It
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
[Example File](ExampleScientist.txt). Add as much of the information
as you can, and try to follow the format as well as you can. If you
send me files (either via email or as a PR), I'll gladly reformat them
to fix any small mistakes, so don't let that stop you!

Please cite your sources (Wikipedia is OK!), and feel free to quote
explicitly, but don't plagiarize!

The python script here autogenerates annotated tables of contents!
Here's the current version, which obviously needs more scientists added:

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
    </tr>
    <tr>
      <th>Chapter</th>
      <th>Section</th>
      <th>Topics</th>
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
    </tr>
    <tr>
      <th>2</th>
      <th></th>
      <th>1D Kinematics</th>
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
    </tr>
    <tr>
      <th>4</th>
      <th></th>
      <th>2D kinematics</th>
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
    </tr>
    <tr>
      <th>6</th>
      <th></th>
      <th>Equilibrium, Mass, Weight, Gravity, Friction, Drag, motion along a line</th>
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
    </tr>
    <tr>
      <th>8</th>
      <th></th>
      <th>Dynamics in a plane</th>
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
    </tr>
    <tr>
      <th>10</th>
      <th></th>
      <th>Energy</th>
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
    </tr>
    <tr>
      <th>12</th>
      <th></th>
      <th>Rotation of a rigid body</th>
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
    </tr>
    <tr>
      <th></th>
      <td>Qiudong Wang</td>
      <td></td>
      <td>Qiudong Wang, mathematical physicist, found an infinite-series solution to the generalized “n-body” problem, which is important in predicting the motions of planetary systems.</td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>Subrahmanyan Chandrasekhar</td>
      <td></td>
      <td>Indian physicist, worked on wide range of astrophysical problems. Developed a theory about the structure of white dwarf stars, placed upper limit on mass of white dwarf stars.</td>
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
    </tr>
    <tr>
      <th rowspan="2" valign="top">15</th>
      <th rowspan="2" valign="top"></th>
      <th>Fluids and elasticity</th>
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
    </tr>
    <tr>
      <th>16</th>
      <th></th>
      <th>Macroscopic description of matter</th>
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
    </tr>
    <tr>
      <th>18</th>
      <th></th>
      <th>Micro/macro connection for gas/thermo, entropy, 2nd law</th>
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
    </tr>
    <tr>
      <th>32</th>
      <th>2</th>
      <th></th>
      <td>Margaret Murnane</td>
      <td><img src="https://jila.colorado.edu/kmlabs/sites/default/files/styles/200_image/public/images/bios/Margaret_Murnane_portrait.jpg?itok=jY-_AF2Q" width="1000"></td>
      <td>Margaret Murnane is an optical physicist at the University of Colorado. She has built "the fastest things that humans have ever created" lasers which can flash for "ten quadrillionths of a second"! Her background includes the fact that "physics was [her] worst subject in high school" but she dreamed of being a physicist because she loved the "excitement of discovery." She and her husband now run a lab at the University of Colorado. In the lab, she records "some of the fastest motions in our natural world." Her lasers can capture the movement of electrons. Her newest laser and x-ray beams can flash for less than 0.00000000000000001 seconds. Talk about "in the blink of an eye!" She is able to pass on excitement and knowledge to students. Scientists use her lasers which are based on her titanium-sapphire design to study a wide range of phenomena (chemical reactoins, etc.).</td>
      <td><a href="https://en.wikipedia.org/wiki/Margaret_Murnane">Link1</a> <a href="https://jila.colorado.edu/kmlabs/bio/murnane">Link2</a></td>
    </tr>
  </tbody>
</table>


And here are some scientists descriptions my students wrote up. Feel
free to add them!

# Scientists

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


## Margaret Murnane

Margaret Mrnane is an optical physicist at the University of
Colorado. She has built "the fastest things that humans have ever
created" lasers which can flash for "ten quadrillionths of a second"!
Her background includes the fact that "physics was [her] worst subject
in high school" but she dreamed of being a physicist because she loved
the "excitement of discovery." She and her husband now run a lab at
the University of Colorado. In the lab, she records "some of the
fastest motions in our natural world." Her lasers can capture the
movement of electrons. Her newest laser and x-ray beams can flash for
less than 0.00000000000000001 seconds. Talk about "in the blink of an
eye!" She is able to pass on excitement and knowledge to
students. Scientists use her lasers which are based on her
titanium-sapphire design to study a wide range of phenomena (chemical
reactoins, etc.).

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

