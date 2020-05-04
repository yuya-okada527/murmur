import React from "react";
import ReactDOM from "react-dom";
import "bootstrap/dist/css/bootstrap.css";

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
        <PostArea />
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
      murmurs: [
        {
          id: 1,
          user_id: "00000001",
          user_name: "user1",
          message: "message1",
          time: "2020-04-23T10:20:30.400+02:30",
        },
        {
          id: 2,
          user_id: "00000002",
          user_name: "user2",
          message: "message2",
          time: "2020-04-27T10:20:30.400+02:30",
        },
      ],
    };
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

const PostArea = (props) => {
  return (
    <form className="form-inline bg-primary">
      <input
        type="text"
        className="form-control mt-2 mb-2 ml-2 col-10"
        placeholder="message"
      />
      <button className="btn btn-success mx-auto m-1 pr-4 pl-4">Murmur</button>
    </form>
  );
};

ReactDOM.render(<TopPage />, document.getElementById("root"));
