import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";
import React, { ReactNode } from "react"

interface State {
  username: string
}

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class MyComponent extends StreamlitComponentBase<State> {
  public state = { username: '' }

  public render = (): ReactNode => {
    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    return (
      <span>
        Hello, {this.state.username}! &nbsp;
      </span>
    )
  }

  componentWillMount() {
    this.getData();
  }

  /** Click handler for our "Click Me!" button. */
  private getData = (): void => {

    const url = this.props.args['url'];

    var self = this;

    fetch(url, { 
      mode: 'no-cors', 
      credentials: 'same-origin',
      headers: new Headers({'Access-Control-Allow-Origin':'*'}) 
    }).then( response => response.json() )
       .then( jr => {
      // update the state of the component with the result here
      console.log(jr);

      // Increment state.numClicks, and pass the new value back to
      // Streamlit via `Streamlit.setComponentValue`.
        this.setState(
          prevState => ({ username: jr.name }),
          () => Streamlit.setComponentValue(self.state.username)
        )

       }
    );

  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
