import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    state = {lat: null, errorMessage: ''};

    componentDidMount() {
        window.navigator.geolocation.getCurrentPosition(
            position => this.setState({lat: position.coords.latitude}),
            err => this.setState({errorMessage: err.message})
        );
    }

    render() {
        return (
            <div className="border">
                Hello this is my app
            </div>
        );
    };
}

ReactDOM.render(<App />, document.getElementById('root'));
