import React from 'react';

export default class AddItem extends React.Component {

    add() {
        this.props.add();
    }

    render() {
        return (
            <div className="col-xs-12 col-sm-6 col-md-4 col-lg-3 list-item-wrapper">
                <div className="list-item add-item">
                    <div className="list-item-header">
                    </div>
                    <div className="list-item-body">
                        <i className="fa fa-plus fa-5x" onClick={this.add.bind(this)}/>
                    </div>
                    <div className="list-item-footer">
                    </div>
                </div>
            </div>
        );
    }

}