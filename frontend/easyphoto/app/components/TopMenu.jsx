import React from 'react';
import {Navbar, NavbarBrand} from 'react-bootstrap';

export default class TopMenu extends React.Component {

    render() {
        return (
            <Navbar fluid={true}>
                <NavbarBrand><img src="/static/images/common/logo.png"/></NavbarBrand>
            </Navbar>
        );
    }
}