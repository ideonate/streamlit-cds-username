import os
import streamlit.components.v1 as components

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

# When we're distributing a production version of the component, we'll
# replace the `url` param with `path`, and point it to to the component's
# build directory:
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("cds_username", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def cds_username(url='/hub/dashboards-api/hub-info/user'):
    """Create a new instance of "cds_username".

    Parameters
    ----------

    string
        url
        default /hub/dashboards-api/hub-info/user

    Returns
    -------
    string
        Username
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(url=url, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value

