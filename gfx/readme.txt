GUIEdgeSmoother by TheThBa

-What this does
ScriptedGui Elements can, unfortunately only be square, and hovering over transparent parts of the element still displays its tooltip. This can be somewhat mitigated with clever layering of elements, but not really avoided.

This aims to change that. Essentially it takes a .bmp image of your GUI with elements that display a tooltip marked in a solid, unique RGB color and converts it into an output of multiple text files that you overlay on top of your GUI.
The tooltips are BGR-color-coded and these tooltips are given in another text file. The x- and y- positions of the created elements should already fit for integration into the GUI.
I personally recommend using a colored sprite for the iconTypes first though - just to get the positions of your container that contains the iconTypes right.

The stacking order of the overlapping iconTypes in your base GUI can (hopefully) be seen from a generated image file called "SquareOverlay.png". If you can't gain much from it - generally iconTypes are ordered top-right to bottom-left.

If my wording here is a bit too unclear or you are having issues with the program not working well, please ping me or DM me on Discord (@TheThba#0244).

-How does it work?

The python script first identifies areas of unique color, lays a square outline around them (to simulate overlap), then specifically takes these overlapping areas and splits them into macropixels (currently up to 5x5 pixels) and rectangles according to an algorithm I've written myself (so expect some possible bugs - I've tested it but you never know), and finally uses these units to create iconTypes of these dimensions at the determined coordinates.

-What is needed?
Enough diskspace and the Python OpenCV library (instructions to install under https://pypi.org/project/opencv-python/) if you don't have it already.
Also obviously something to run python scripts on - I use Spyder, but you can probably use whatever you usually use.

Are there limitations?

Yes. If too many GUI elements are added, lag becomes an issue. This must be determined by you on a case by case basis.