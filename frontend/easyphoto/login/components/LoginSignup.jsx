import React from 'react';

export default class LoginSignup extends React.Component {

    render() {
        return (
            <div className="login-signup">
                {this.props.children}
            </div>
        );
    }
}