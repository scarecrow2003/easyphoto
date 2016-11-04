import React from 'react';
import {Form} from 'react-bootstrap';

export default class ValidatedFormHorizontal extends React.Component {

    constructor(){
        super();
    }

    componentWillMount(){

    }

    render() {
        var self = this;
        return (
            <Form className="col-xs-12" {...this.props}>
                {this.props.children}
            </Form>);
    }
}

