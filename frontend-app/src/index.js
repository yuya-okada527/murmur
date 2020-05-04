import React from "react";
import ReactDOM from "react-dom";

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
      <div>
        <Header title="Murmur" />
        <Murmurs />
        <PostArea />
      </div>
    );
  }
}

const Header = (props) => {
  return (
    <div>
      <h1>{props.title}</h1>
    </div>
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
        <div>
          <li key={murmur.id}>
            <Murmur value={murmur} />
          </li>
        </div>
      );
    });
    return <div>{murmurs}</div>;
  }
}

const Murmur = (props) => {
  return (
    <div class="card">
      <div class="user-info">
        {props.value.user_name + "@" + props.value.user_id}
      </div>
      <div class="message-area">{props.value.message}</div>
    </div>
  );
};

const PostArea = (props) => {
  return (
    <form>
      <input></input>
      <button />
    </form>
  );
};

ReactDOM.render(<TopPage />, document.getElementById("root"));
