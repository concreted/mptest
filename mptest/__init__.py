import time
import numpy as np
import cv2

def noop(input):
    return input

def print_n(id, n):
    for i in range(n):
        print(f"{id}: {i}")

def crash(input):
    raise Exception(f"{input}")

def fill_text(id, n):
    text = """
    “Why do paints and varnishes crack, and what is the reason that cracks in the latter are usually at right angles to the grain of the wood?”

    [21]

    The subject, as I understand it, relates to the cracking of varnishes, etc., as experienced in connection with passenger car work, and as such I introduce it for discussion before this association.

    There are many theories as to the cause of the cracking of paints and varnishes. Some are well defined, others are not satisfactorily explained.

    I do not anticipate being able to add much to what is already known, but will advance a few thoughts, which may call forth the views of others on the subject.

    The old adage, “It takes two to make a quarrel,” is as true when applied to paints and varnishes as it is to individuals. A single coat of either seldom, if ever, produces cracks. These make their appearance only after two or more coats have been applied; consequently, it is necessary to have a body of color or varnish, consisting of two or more coats, before any trouble of this kind makes itself manifest.

    This being the case, it follows that the cause of the difficulty must be sought for in the coatings themselves, either in the quality of the material employed or in the mode of applying them.

    Poor and cheap oils and japans—especially the latter—are a fruitful source of cracking in paint; but by far the most prolific one, in my opinion, is the hurried application of the succeeding coats before the preceding ones are dry enough to receive them.[22] If sufficient time is not given, cracks will inevitably follow such a mode of procedure.

    I am of the opinion, also, that very little blame can be attached to the wood used in the construction of cars, as most of it is comparatively well seasoned, and its expansive and contractive force is not sufficient to cause serious trouble. If green wood was used there might be room for this excuse, especially where the cracks run in the direction of the grain, and are large and deep.

    Before pursuing this subject further, it may be well to examine a little into the theory of the drying of paint. It is purely a chemical process, not a mechanical one, as some suppose. Paint dries by the evaporation of its volatile parts and its absorption of oxygen; it is heavier when dried than when in the liquid form, having attached to itself a sufficient amount of oxygen to very perceptibly increase the weight some 6 per cent.

    The best grades of linseed oil are said to contain from 70 to 80 per cent. of substance called linoleine, a resinous and slow-drying oil and acid which imparts to the oil its elasticity.

    In the process of drying, contraction occurs. The various atoms of which the coatings are composed move closer and closer together; and as this contracting force is easier with than across the grain, cracks at right angles to it are formed. This fact suggests the necessity of so adjusting the elasticity[23] of the various coats that the force exerted in drying may be as nearly equalized as possible, as their contracting force is continued until all elasticity has left the paint and oxygen ceases to be absorbed, all the oil acid has disappeared, and nothing but a hard, brittle surface remains.

    Under the microscope, in the first stage of cracking, the surface presents nothing unusual except that the cracks appear clean cut and sharp on the edges. As months pass by and the surface is exposed to the atmospheric changes of heat and cold, wet and dry, the cracks become more numerous; and in the last stage, when the oil is entirely destroyed, the surface assumes the appearance of innumerable rectangular masses, higher in the center than at the edges, like small mounds raised by the process of contraction and adhesion.

    Cracking in color coats may, by careful attention to preliminaries, be reduced to a minimum, provided good first-class materials are used and sufficient time is given to each coat to dry.

    Where varnish is to be applied as a finish, all coatings should have oil in their composition and yet be mixed to dry flat. They should be applied very evenly and thinly, even if it necessitates an extra coat, to cover and make a solid job.

    Striping and ornamenting should be done on flat color, which gives time for hardening, and fits it for[24] the varnish coats to follow. If work is done in this way, I think very little fear of premature cracking need be entertained; at least, not until time and weather have sufficient opportunity to play havoc with its beauty, and natural decay of the materials themselves necessitates a thorough overhauling and repairing.

    Rubbing varnishes are another source of trouble, causing the succeeding coats of finishing varnish to show signs of cracking long before they otherwise would, as it does not agree with the slower drying varnishes usually applied above it, being of a harder and more brittle character, serving the purpose of producing a fine, smooth surface, but sacrificing the durability of the job.

    Concerning the cracking of varnish, I have not much to say. It seems to me that many of the reasons given above will apply to it as well as to the paint.

    Poor material in the shape of varnish is poor indeed. A first-class article only will give first-class results.

    It must be elastic, or it will crack easily and badly, no matter how good the undercoats of paint may be.

    Good varnish on good color coats will not give any signs of cracking until, by repeated varnishings, it has accumulated a thick coating of brittle, unelastic gum.

    [25]

    No painter can say truthfully that his cars never crack, as it is a natural consequence of decay, and will come, sooner or later, to the best of material.

    That varnish cracks to a great extent at right angles to the grain of the wood, I think is due, in some degree, to the same reasons as given above for the cracking of paint, and after its elasticity is destroyed by age. Vibration has a great effect upon the hard and brittle coating of gum that remains, coupled with expansion and contraction caused by variations of temperature and the disintegrating influences of the weather.
    """
    for i in range(n):
        print(text)

def use_mem(input, units, amount):
    size = 1024*1024
    if units == "gb":
        size = size * 1024
    size = size * amount
    x = bytearray()

def opencv(input):
    rgb_img = np.zeros((500, 500, 3))
    bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"/tmp/{input}", bgr_img)
