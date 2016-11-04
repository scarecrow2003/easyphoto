import React from 'react';

export default class ListItem extends React.Component {

    getTitle() {

    }

    getBody() {

    }

    deleteItem() {

    }

    editItem() {

    }

    render() {
        const title = this.getTitle();
        const body = this.getBody();
        return (
            <div className="col-xs-12 col-sm-6 col-md-4 col-lg-3 list-item-wrapper">
                <div className="list-item">
                    <div className="list-item-header">
                        <h4 className="list-item-title">{title}</h4>
                    </div>
                    <div className="list-item-body">
                        {body}
                    </div>
                    <div className="list-item-footer">
                        <div className="col-xs-6 list-item-button">
                            <button onClick={this.editItem.bind(this)}><i className="fa fa-pencil"></i>Edit</button>
                        </div>
                        <div className="col-xs-6 list-item-button">
                            <button className="red-button" onClick={this.deleteItem.bind(this)}><i className="fa fa-trash"></i>Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}