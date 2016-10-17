import React from 'react';
import TopMenu from './TopMenu';

export default class Home extends React.Component {
    render() {
        return (
            <div className="col-xs-12 home">
                <div className="col-xs-12">
                    <TopMenu />
                </div>
                <div className="col-xs-12 main-panel">
                    <div className="col-xs-12 panel-wrapper">
                        {this.props.children}
                    </div>
                </div>
            </div>
        );
    }
}
