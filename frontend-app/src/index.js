import React from "react";
import ReactDOM from "react-dom";
import "bootstrap/dist/css/bootstrap.css";

const URL = "http://localhost:8000";

async function callApiByPost(path, body) {
  const url = URL + path;
  const method = "POST";
  const headers = {
    Accept: "application/json",
    "Content-Type": "application/json",
  };
  const response = await fetch(url, {
    method,
    headers,
    body,
  });
  return response;
}

async function callApiByGet(path) {
  const url = URL + path;
  const method = "GET";
  const headers = {
    Accept: "application/json",
    "Content-Type": "application/json",
  };
  const response = await fetch(url, {
    method,
    headers,
  })
    .then((res) => res.text())
    .then((body) => JSON.parse(body));

  return response;
}

class TopPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {
        user_id: "12345678",
        user_name: "user",
      },
    };
  }

  render() {
    return (
      <div className="container">
        <Header title="Murmur" />
        <Murmurs />
        <PostArea user={this.state.user} />
      </div>
    );
  }
}

const Header = (props) => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary mt-4 mb-4">
      <h1 className="m-1 navbar-brand">{props.title}</h1>
    </nav>
  );
};

class Murmurs extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      murmurs: [],
    };
    this.fetchAll();
  }

  async fetchAll() {
    const path = "/murmurs/all";
    const response = await callApiByGet(path);
    this.setState({
      murmurs: response.result,
    });
  }

  render() {
    const murmurs = this.state.murmurs.map((murmur) => {
      return (
        <ul className="list-unstyled">
          <li key={murmur.id}>
            <Murmur value={murmur} />
          </li>
        </ul>
      );
    });
    return <div>{murmurs}</div>;
  }
}

const Murmur = (props) => {
  return (
    <div className="card border-primary">
      <div className="card-header">
        {props.value.user_name + "@" + props.value.user_id}
      </div>
      <div className="card-body card-text mr-3 ml-3">{props.value.message}</div>
    </div>
  );
};

class PostArea extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: props.user,
      message: "",
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(event) {
    this.createMurmur();
    event.preventDefault();
    this.setState({
      user: this.state.user,
      message: "",
    });
  }

  handleChange(event) {
    this.setState({
      user: this.state.user,
      message: event.target.value,
    });
  }

  createMurmur() {
    const path = "/murmurs";
    const body = JSON.stringify({
      user_id: this.state.user.user_id,
      user_name: this.state.user.user_name,
      message: this.state.message,
    });
    callApiByPost(path, body);
  }

  render() {
    return (
      <form className="form-inline bg-primary mb-5">
        <input
          type="text"
          className="form-control mt-2 mb-2 ml-2 col-10"
          placeholder="message"
          onChange={this.handleChange}
        />
        <input
          type="submit"
          value="Murmur"
          className="btn btn-success mx-auto m-1 pr-4 pl-4"
          onClick={this.handleClick}
        />
      </form>
    );
  }
}

ReactDOM.render(<TopPage />, document.getElementById("root"));
