import React from 'react';
import {Modal} from 'react-bootstrap';

export default class ModalComponent extends React.Component {

    constructor() {
        super();
        this.state = this._getInitialState();
    }

    _getInitialState() {
        return {
            showModal: false,
            title:''
        };
    }

    componentDidMount() {

    }

    close(){
        this.props.close();
    }

    open(){
        this.props.open();
    }

    componentWillReceiveProps(newProps) {
        this.setState({
            showModal: newProps.showModal,
            title: newProps.title
        });
    }

    render() {
        return (
            <Modal show={this.state.showModal} onHide={this.close.bind(this)} bsSize={this.props.bsSize}>
                <Modal.Header closeButton>
                    <Modal.Title>{this.state.title}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    {this.props.children}
                </Modal.Body>
                <Modal.Footer>
                    {this.props.actions.map(function(action,i){
                        return (action);
                    })}
                </Modal.Footer>
            </Modal>
        )
    }
};