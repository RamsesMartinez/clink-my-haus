import { library, dom } from '@fortawesome/fontawesome-svg-core'
import { faPhone } from '@fortawesome/free-solid-svg-icons'

import { faFacebookF, faInstagram, faTwitter, faWhatsapp} from '@fortawesome/free-brands-svg-icons'

library.add(faPhone, faInstagram, faFacebookF, faTwitter, faWhatsapp);

dom.i2svg();
