import cookie from 'react-cookie';

class Cookie {

    getUser() {
        let user = cookie.load('epuser', {path:'/'});
        if (user) {
            return JSON.parse(cookie.load('gm-client',{path:'/'}));
        } else {
            return null;
        }
    }
}

export default new Cookie()