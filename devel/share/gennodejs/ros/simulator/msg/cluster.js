// Auto-generated. Do not edit!

// (in-package simulator.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let event = require('./event.js');

//-----------------------------------------------------------

class cluster {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cluster_id = null;
      this.size = null;
      this.events = null;
    }
    else {
      if (initObj.hasOwnProperty('cluster_id')) {
        this.cluster_id = initObj.cluster_id
      }
      else {
        this.cluster_id = 0;
      }
      if (initObj.hasOwnProperty('size')) {
        this.size = initObj.size
      }
      else {
        this.size = 0;
      }
      if (initObj.hasOwnProperty('events')) {
        this.events = initObj.events
      }
      else {
        this.events = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type cluster
    // Serialize message field [cluster_id]
    bufferOffset = _serializer.int32(obj.cluster_id, buffer, bufferOffset);
    // Serialize message field [size]
    bufferOffset = _serializer.int32(obj.size, buffer, bufferOffset);
    // Serialize message field [events]
    // Serialize the length for message field [events]
    bufferOffset = _serializer.uint32(obj.events.length, buffer, bufferOffset);
    obj.events.forEach((val) => {
      bufferOffset = event.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type cluster
    let len;
    let data = new cluster(null);
    // Deserialize message field [cluster_id]
    data.cluster_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [size]
    data.size = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [events]
    // Deserialize array length for message field [events]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.events = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.events[i] = event.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.events.forEach((val) => {
      length += event.getMessageSize(val);
    });
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'simulator/cluster';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'be8d7800e24ef3d0dd2a228257781b9f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 cluster_id
    int32 size
    event[] events
    ================================================================================
    MSG: simulator/event
    string generator_id
    int32 ID
    string type
    time generation_date
    string gen_time
    time completed_date
    string compl_time
    string[] route
    string split_attribute1
    float32 split1
    string split_attribute2
    float32 split2
    string split_attribute3
    float32 split3
    string attribute2
    float32 value2
    string attribute3
    float32 value3
    bool last_event
    bool first_event
    
    
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new cluster(null);
    if (msg.cluster_id !== undefined) {
      resolved.cluster_id = msg.cluster_id;
    }
    else {
      resolved.cluster_id = 0
    }

    if (msg.size !== undefined) {
      resolved.size = msg.size;
    }
    else {
      resolved.size = 0
    }

    if (msg.events !== undefined) {
      resolved.events = new Array(msg.events.length);
      for (let i = 0; i < resolved.events.length; ++i) {
        resolved.events[i] = event.Resolve(msg.events[i]);
      }
    }
    else {
      resolved.events = []
    }

    return resolved;
    }
};

module.exports = cluster;
