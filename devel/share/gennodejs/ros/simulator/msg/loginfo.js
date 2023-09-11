// Auto-generated. Do not edit!

// (in-package simulator.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class loginfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ID_node = null;
      this.type = null;
      this.node_name = null;
      this.server_time = null;
      this.num_servers = null;
      this.utiliz_tot = null;
      this.utiliz_array = null;
      this.utiliz_array_tot = null;
      this.queue_array = null;
      this.time_array = null;
      this.time_array_intervals = null;
      this.queue_left = null;
      this.event_processed = null;
      this.info = null;
      this.ready = null;
      this.events_left = null;
      this.start = null;
      this.start_esecution = null;
      this.stop_esecution = null;
      this.statistic = null;
    }
    else {
      if (initObj.hasOwnProperty('ID_node')) {
        this.ID_node = initObj.ID_node
      }
      else {
        this.ID_node = 0;
      }
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = '';
      }
      if (initObj.hasOwnProperty('node_name')) {
        this.node_name = initObj.node_name
      }
      else {
        this.node_name = '';
      }
      if (initObj.hasOwnProperty('server_time')) {
        this.server_time = initObj.server_time
      }
      else {
        this.server_time = 0.0;
      }
      if (initObj.hasOwnProperty('num_servers')) {
        this.num_servers = initObj.num_servers
      }
      else {
        this.num_servers = 0.0;
      }
      if (initObj.hasOwnProperty('utiliz_tot')) {
        this.utiliz_tot = initObj.utiliz_tot
      }
      else {
        this.utiliz_tot = 0.0;
      }
      if (initObj.hasOwnProperty('utiliz_array')) {
        this.utiliz_array = initObj.utiliz_array
      }
      else {
        this.utiliz_array = [];
      }
      if (initObj.hasOwnProperty('utiliz_array_tot')) {
        this.utiliz_array_tot = initObj.utiliz_array_tot
      }
      else {
        this.utiliz_array_tot = [];
      }
      if (initObj.hasOwnProperty('queue_array')) {
        this.queue_array = initObj.queue_array
      }
      else {
        this.queue_array = [];
      }
      if (initObj.hasOwnProperty('time_array')) {
        this.time_array = initObj.time_array
      }
      else {
        this.time_array = [];
      }
      if (initObj.hasOwnProperty('time_array_intervals')) {
        this.time_array_intervals = initObj.time_array_intervals
      }
      else {
        this.time_array_intervals = [];
      }
      if (initObj.hasOwnProperty('queue_left')) {
        this.queue_left = initObj.queue_left
      }
      else {
        this.queue_left = 0;
      }
      if (initObj.hasOwnProperty('event_processed')) {
        this.event_processed = initObj.event_processed
      }
      else {
        this.event_processed = 0;
      }
      if (initObj.hasOwnProperty('info')) {
        this.info = initObj.info
      }
      else {
        this.info = '';
      }
      if (initObj.hasOwnProperty('ready')) {
        this.ready = initObj.ready
      }
      else {
        this.ready = false;
      }
      if (initObj.hasOwnProperty('events_left')) {
        this.events_left = initObj.events_left
      }
      else {
        this.events_left = 0;
      }
      if (initObj.hasOwnProperty('start')) {
        this.start = initObj.start
      }
      else {
        this.start = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('start_esecution')) {
        this.start_esecution = initObj.start_esecution
      }
      else {
        this.start_esecution = false;
      }
      if (initObj.hasOwnProperty('stop_esecution')) {
        this.stop_esecution = initObj.stop_esecution
      }
      else {
        this.stop_esecution = false;
      }
      if (initObj.hasOwnProperty('statistic')) {
        this.statistic = initObj.statistic
      }
      else {
        this.statistic = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type loginfo
    // Serialize message field [ID_node]
    bufferOffset = _serializer.int32(obj.ID_node, buffer, bufferOffset);
    // Serialize message field [type]
    bufferOffset = _serializer.string(obj.type, buffer, bufferOffset);
    // Serialize message field [node_name]
    bufferOffset = _serializer.string(obj.node_name, buffer, bufferOffset);
    // Serialize message field [server_time]
    bufferOffset = _serializer.float32(obj.server_time, buffer, bufferOffset);
    // Serialize message field [num_servers]
    bufferOffset = _serializer.float32(obj.num_servers, buffer, bufferOffset);
    // Serialize message field [utiliz_tot]
    bufferOffset = _serializer.float32(obj.utiliz_tot, buffer, bufferOffset);
    // Serialize message field [utiliz_array]
    bufferOffset = _arraySerializer.float32(obj.utiliz_array, buffer, bufferOffset, null);
    // Serialize message field [utiliz_array_tot]
    bufferOffset = _arraySerializer.float32(obj.utiliz_array_tot, buffer, bufferOffset, null);
    // Serialize message field [queue_array]
    bufferOffset = _arraySerializer.float32(obj.queue_array, buffer, bufferOffset, null);
    // Serialize message field [time_array]
    bufferOffset = _arraySerializer.time(obj.time_array, buffer, bufferOffset, null);
    // Serialize message field [time_array_intervals]
    bufferOffset = _arraySerializer.time(obj.time_array_intervals, buffer, bufferOffset, null);
    // Serialize message field [queue_left]
    bufferOffset = _serializer.int32(obj.queue_left, buffer, bufferOffset);
    // Serialize message field [event_processed]
    bufferOffset = _serializer.int32(obj.event_processed, buffer, bufferOffset);
    // Serialize message field [info]
    bufferOffset = _serializer.string(obj.info, buffer, bufferOffset);
    // Serialize message field [ready]
    bufferOffset = _serializer.bool(obj.ready, buffer, bufferOffset);
    // Serialize message field [events_left]
    bufferOffset = _serializer.int32(obj.events_left, buffer, bufferOffset);
    // Serialize message field [start]
    bufferOffset = _serializer.time(obj.start, buffer, bufferOffset);
    // Serialize message field [start_esecution]
    bufferOffset = _serializer.bool(obj.start_esecution, buffer, bufferOffset);
    // Serialize message field [stop_esecution]
    bufferOffset = _serializer.bool(obj.stop_esecution, buffer, bufferOffset);
    // Serialize message field [statistic]
    bufferOffset = _serializer.bool(obj.statistic, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type loginfo
    let len;
    let data = new loginfo(null);
    // Deserialize message field [ID_node]
    data.ID_node = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [type]
    data.type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [node_name]
    data.node_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [server_time]
    data.server_time = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [num_servers]
    data.num_servers = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [utiliz_tot]
    data.utiliz_tot = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [utiliz_array]
    data.utiliz_array = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [utiliz_array_tot]
    data.utiliz_array_tot = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [queue_array]
    data.queue_array = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [time_array]
    data.time_array = _arrayDeserializer.time(buffer, bufferOffset, null)
    // Deserialize message field [time_array_intervals]
    data.time_array_intervals = _arrayDeserializer.time(buffer, bufferOffset, null)
    // Deserialize message field [queue_left]
    data.queue_left = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [event_processed]
    data.event_processed = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [info]
    data.info = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [ready]
    data.ready = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [events_left]
    data.events_left = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [start]
    data.start = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [start_esecution]
    data.start_esecution = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [stop_esecution]
    data.stop_esecution = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [statistic]
    data.statistic = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.type);
    length += _getByteLength(object.node_name);
    length += 4 * object.utiliz_array.length;
    length += 4 * object.utiliz_array_tot.length;
    length += 4 * object.queue_array.length;
    length += 8 * object.time_array.length;
    length += 8 * object.time_array_intervals.length;
    length += _getByteLength(object.info);
    return length + 72;
  }

  static datatype() {
    // Returns string type for a message object
    return 'simulator/loginfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '55d87199e7f17ce94759f154f0e8ee23';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 ID_node
    string type
    string node_name
    
    float32 server_time
    float32 num_servers
    float32 utiliz_tot
    float32[] utiliz_array
    float32[] utiliz_array_tot
    float32[] queue_array
    time[] time_array
    time[] time_array_intervals
    int32 queue_left
    int32 event_processed
    string info
    bool ready
    
    int32 events_left
    time start
    
    bool start_esecution
    bool stop_esecution
    bool statistic
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new loginfo(null);
    if (msg.ID_node !== undefined) {
      resolved.ID_node = msg.ID_node;
    }
    else {
      resolved.ID_node = 0
    }

    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = ''
    }

    if (msg.node_name !== undefined) {
      resolved.node_name = msg.node_name;
    }
    else {
      resolved.node_name = ''
    }

    if (msg.server_time !== undefined) {
      resolved.server_time = msg.server_time;
    }
    else {
      resolved.server_time = 0.0
    }

    if (msg.num_servers !== undefined) {
      resolved.num_servers = msg.num_servers;
    }
    else {
      resolved.num_servers = 0.0
    }

    if (msg.utiliz_tot !== undefined) {
      resolved.utiliz_tot = msg.utiliz_tot;
    }
    else {
      resolved.utiliz_tot = 0.0
    }

    if (msg.utiliz_array !== undefined) {
      resolved.utiliz_array = msg.utiliz_array;
    }
    else {
      resolved.utiliz_array = []
    }

    if (msg.utiliz_array_tot !== undefined) {
      resolved.utiliz_array_tot = msg.utiliz_array_tot;
    }
    else {
      resolved.utiliz_array_tot = []
    }

    if (msg.queue_array !== undefined) {
      resolved.queue_array = msg.queue_array;
    }
    else {
      resolved.queue_array = []
    }

    if (msg.time_array !== undefined) {
      resolved.time_array = msg.time_array;
    }
    else {
      resolved.time_array = []
    }

    if (msg.time_array_intervals !== undefined) {
      resolved.time_array_intervals = msg.time_array_intervals;
    }
    else {
      resolved.time_array_intervals = []
    }

    if (msg.queue_left !== undefined) {
      resolved.queue_left = msg.queue_left;
    }
    else {
      resolved.queue_left = 0
    }

    if (msg.event_processed !== undefined) {
      resolved.event_processed = msg.event_processed;
    }
    else {
      resolved.event_processed = 0
    }

    if (msg.info !== undefined) {
      resolved.info = msg.info;
    }
    else {
      resolved.info = ''
    }

    if (msg.ready !== undefined) {
      resolved.ready = msg.ready;
    }
    else {
      resolved.ready = false
    }

    if (msg.events_left !== undefined) {
      resolved.events_left = msg.events_left;
    }
    else {
      resolved.events_left = 0
    }

    if (msg.start !== undefined) {
      resolved.start = msg.start;
    }
    else {
      resolved.start = {secs: 0, nsecs: 0}
    }

    if (msg.start_esecution !== undefined) {
      resolved.start_esecution = msg.start_esecution;
    }
    else {
      resolved.start_esecution = false
    }

    if (msg.stop_esecution !== undefined) {
      resolved.stop_esecution = msg.stop_esecution;
    }
    else {
      resolved.stop_esecution = false
    }

    if (msg.statistic !== undefined) {
      resolved.statistic = msg.statistic;
    }
    else {
      resolved.statistic = false
    }

    return resolved;
    }
};

module.exports = loginfo;
