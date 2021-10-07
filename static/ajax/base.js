export default class sendMsg {
    static done = (statusCode, textStatus, msg) => {
        console.log(`${msg} ${statusCode} (${textStatus})`);
    }
    static fail = (statusCode, textStatus, msg) => {
        alert(`${msg} ${statusCode} (${textStatus})`);
    }
}
