import React from 'react';
import {Button} from 'react-bootstrap';
import TopMenu from './TopMenu';
import {LOGIN_STRINGS} from '../../common/utils/Localization';
import Cookie from '../../common/utils/Cookie';

export default class Home extends React.Component {

    constructor() {
        super();
        this.state = {
            user: null//{id: 123, name: 'abc', gid: 234}
        }
        this.login = this.login.bind(this);
    }

    componentWillMount() {
        let user = Cookie.getUser();
        if (user) {
            this.setState({user: user});
        }
    }

    login() {
        console.log('login');
    }

    render() {
        return (
            <div className="col-xs-12 home">
                <div className="col-xs-12">
                    <TopMenu />
                </div>
                <div className="col-xs-12 main-panel">
                    <div className="col-xs-12 panel-wrapper">
                        {this.state.user==null?
                        <div className="login-container"><span>{LOGIN_STRINGS.notlogin} </span><Button onClick={this.login}>{LOGIN_STRINGS.login}</Button></div>
                        :(this.props.children?this.props.children
                        :<div>
                            <span>{'You have {0} jobs pending'.replace('{0}', 10)}</span>
                        </div>)}
                    </div>
                </div>
            </div>
        );
    }
}
