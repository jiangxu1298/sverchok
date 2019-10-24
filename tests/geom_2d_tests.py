from sverchok.utils.testing import SverchokTestCase
from sverchok.utils.geom_2d.make_monotone import monotone_sv_face_with_holes


class MakeMonotoneTest(SverchokTestCase):
    def test_one_face(self):
        # https://user-images.githubusercontent.com/28003269/67469986-13241000-f65e-11e9-85c4-7656f1ae16a5.png
        main_face = [[2.309999942779541,0.0,0.0],[1.7819089889526367,-0.5280910134315491,0.0],[1.7819087505340576,-1.7819093465805054,0.0],[0.7080908417701721,-1.7819091081619263,0.0],[2.969295209709344e-08,-2.490000009536743,0.0],[-0.7505173683166504,-1.7394826412200928,0.0],[-1.7394828796386719,-1.7394825220108032,0.0],[-1.7394826412200928,-0.6905173659324646,0.0],[-2.430000066757202,-2.12437356594819e-07,0.0],[-1.6970562934875488,0.7329436540603638,0.0],[-1.6970562934875488,1.6970562934875488,0.0],[-0.6729437708854675,1.6970562934875488,0.0],[-1.0359598690001803e-07,2.369999885559082,0.0],[0.7153699994087219,1.6546299457550049,0.0],[1.6546298265457153,1.6546298265457153,0.0],[1.6546299457550049,0.6553700566291809,0.0]]
        vert_hols = [[0.7099999785423279,9.797174820681343e-17,0.0],[0.48083260655403137,0.48083260655403137,0.0],[-2.841240132056555e-08,0.6499999761581421,0.0],[-0.43840619921684265,0.43840619921684265,0.0],[-0.5899999737739563,-5.157943760991657e-08,0.0],[-0.3959798216819763,-0.39597976207733154,0.0],[6.320186596298072e-09,-0.5299999713897705,0.0],[0.35355329513549805,-0.3535534143447876,0.0],[0.48083263635635376,1.1308326721191406,0.0],[-0.43840622901916504,1.0884062051773071,0.0],[1.1908326148986816,0.48083263635635376,0.0],[-1.0284063816070557,0.43840619921684265,0.0],[1.0635534524917603,-0.35355353355407715,0.0],[-0.9859795570373535,-0.39597970247268677,0.0],[0.3535532057285309,-0.883553147315979,0.0],[-0.3959798514842987,-0.9259797930717468,0.0],[1.8600000143051147,0.0,0.0],[1.5099999904632568,0.3500000536441803,0.0],[1.159999966621399,4.2862643149203325e-17,0.0],[1.5099999904632568,-0.3500000536441803,0.0],[1.3364317417144775,1.3364317417144775,0.0],[0.7990306615829468,1.336431860923767,0.0],[0.7990306615829468,0.7990306615829468,0.0],[1.336431860923767,0.7990306615829468,0.0],[-8.392586892114196e-08,1.9200000762939453,0.0],[-0.41000011563301086,1.5099999904632568,0.0],[-4.808252285215531e-08,1.0999999046325684,0.0],[0.4099999964237213,1.5099999904632568,0.0],[-1.378858208656311,1.378858208656311,0.0],[-1.3788583278656006,0.7566042542457581,0.0],[-0.7566041946411133,0.7566041946411133,0.0],[-0.7566042542457581,1.3788583278656006,0.0],[-1.9800000190734863,-1.730970922153574e-07,0.0],[-1.5099999904632568,-0.47000017762184143,0.0],[-1.0399999618530273,-9.091968422580976e-08,0.0],[-1.5099999904632568,0.46999993920326233,0.0],[-1.4212846755981445,-1.4212844371795654,0.0],[-0.7141778469085693,-1.421284556388855,0.0],[-0.7141779065132141,-0.7141777873039246,0.0],[-1.4212846755981445,-0.7141777276992798,0.0],[2.4326755720949222e-08,-2.0399999618530273,0.0],[0.5300000309944153,-1.5099999904632568,0.0],[1.1686382528353079e-08,-0.9799999594688416,0.0],[-0.5300000309944153,-1.5099999904632568,0.0],[1.4637106657028198,-1.4637112617492676,0.0],[1.463710904121399,-0.6717516183853149,0.0],[0.6717512607574463,-0.6717514991760254,0.0],[0.6717511415481567,-1.463711142539978,0.0]]
        face_hols = [[0,12,7,14,6,15,5,13,4,11,3,9,2,8,1,10],[16,19,18,17],[20,23,22,21],[24,27,26,25],[28,31,30,29],[32,35,34,33],[36,39,38,37],[40,43,42,41],[44,47,46,45]]

        vert_expect_result = [[1.6546299457550049,0.6553700566291809,0.0],[1.6546298265457153,1.6546298265457153,0.0],[0.7153699994087219,1.6546299457550049,0.0],[-1.0359598690001803e-07,2.369999885559082,0.0],[-0.6729437708854675,1.6970562934875488,0.0],[-1.6970562934875488,1.6970562934875488,0.0],[-1.6970562934875488,0.7329436540603638,0.0],[-2.430000066757202,-2.12437356594819e-07,0.0],[-1.7394826412200928,-0.6905173659324646,0.0],[-1.7394828796386719,-1.7394825220108032,0.0],[-0.7505173683166504,-1.7394826412200928,0.0],[2.969295209709344e-08,-2.490000009536743,0.0],[0.7080908417701721,-1.7819091081619263,0.0],[1.7819087505340576,-1.7819093465805054,0.0],[1.7819089889526367,-0.5280910134315491,0.0],[2.309999942779541,0.0,0.0],[1.1908326148986816,0.48083263635635376,0.0],[0.48083260655403137,0.48083260655403137,0.0],[0.48083263635635376,1.1308326721191406,0.0],[-2.841240132056555e-08,0.6499999761581421,0.0],[-0.43840622901916504,1.0884062051773071,0.0],[-0.43840619921684265,0.43840619921684265,0.0],[-1.0284063816070557,0.43840619921684265,0.0],[-0.5899999737739563,-5.157943760991657e-08,0.0],[-0.9859795570373535,-0.39597970247268677,0.0],[-0.3959798216819763,-0.39597976207733154,0.0],[-0.3959798514842987,-0.9259797930717468,0.0],[6.320186596298072e-09,-0.5299999713897705,0.0],[0.3535532057285309,-0.883553147315979,0.0],[0.35355329513549805,-0.3535534143447876,0.0],[1.0635534524917603,-0.35355353355407715,0.0],[0.7099999785423279,9.797174820681343e-17,0.0],[1.5099999904632568,0.3500000536441803,0.0],[1.159999966621399,4.2862643149203325e-17,0.0],[1.5099999904632568,-0.3500000536441803,0.0],[1.8600000143051147,0.0,0.0],[0.7990306615829468,1.336431860923767,0.0],[0.7990306615829468,0.7990306615829468,0.0],[1.336431860923767,0.7990306615829468,0.0],[1.3364317417144775,1.3364317417144775,0.0],[-0.41000011563301086,1.5099999904632568,0.0],[-4.808252285215531e-08,1.0999999046325684,0.0],[0.4099999964237213,1.5099999904632568,0.0],[-8.392586892114196e-08,1.9200000762939453,0.0],[-1.3788583278656006,0.7566042542457581,0.0],[-0.7566041946411133,0.7566041946411133,0.0],[-0.7566042542457581,1.3788583278656006,0.0],[-1.378858208656311,1.378858208656311,0.0],[-1.5099999904632568,-0.47000017762184143,0.0],[-1.0399999618530273,-9.091968422580976e-08,0.0],[-1.5099999904632568,0.46999993920326233,0.0],[-1.9800000190734863,-1.730970922153574e-07,0.0],[-0.7141778469085693,-1.421284556388855,0.0],[-0.7141779065132141,-0.7141777873039246,0.0],[-1.4212846755981445,-0.7141777276992798,0.0],[-1.4212846755981445,-1.4212844371795654,0.0],[0.5300000309944153,-1.5099999904632568,0.0],[1.1686382528353079e-08,-0.9799999594688416,0.0],[-0.5300000309944153,-1.5099999904632568,0.0],[2.4326755720949222e-08,-2.0399999618530273,0.0],[1.463710904121399,-0.6717516183853149,0.0],[0.6717512607574463,-0.6717514991760254,0.0],[0.6717511415481567,-1.463711142539978,0.0],[1.4637106657028198,-1.4637112617492676,0.0]]
        face_expect_result = [[3,43,42,36,39,38,0,1,2],[43,3,4,40],[40,4,5,6,45,44,47],[50,6,7,8,48,51],[54,8,9,10,11,59,58,52,55],[12,56,59,11],[14,61,60,63,56,12,13],[36,18,17,16,32,35,34,30,14,15,0,38,37],[36,42,41,20,19,18],[40,47,46,45,6,50,22,21,20,41],[22,50,49,48,8,54,53,52,58,57,26,25,24,23],[26,28,27],[14,30,29,28,26,57,56,63,62,61],[32,16,31,30,34,33]]

        vert_result, face_result = monotone_sv_face_with_holes(main_face, vert_hols, face_hols, accuracy=5)

        self.assert_sverchok_data_equal(vert_expect_result, vert_result, precision=5)
        self.assert_sverchok_data_equal(face_expect_result, face_result)

