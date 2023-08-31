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

class event {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.generator_id = null;
      this.ID = null;
      this.type = null;
      this.generation_date = null;
      this.gen_time = null;
      this.completed_date = null;
      this.compl_time = null;
      this.route = null;
      this.split_attribute1 = null;
      this.split1 = null;
      this.split_attribute2 = null;
      this.split2 = null;
      this.split_attribute3 = null;
      this.split3 = null;
      this.attribute2 = null;
      this.value2 = null;
      this.attribute3 = null;
      this.value3 = null;
      this.last_event = null;
    }
    else {
      if (initObj.hasOwnProperty('generator_id')) {
        this.generator_id = initObj.generator_id
      }
      else {
        this.generator_id = '';
      }
      if (initObj.hasOwnProperty('ID')) {
        this.ID = initObj.ID
      }
      else {
        this.ID = 0;
      }
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = '';
      }
      if (initObj.hasOwnProperty('generation_date')) {
        this.generation_date = initObj.generation_date
      }
      else {
        this.generation_date = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('gen_time')) {
        this.gen_time = initObj.gen_time
      }
      else {
        this.gen_time = '';
      }
      if (initObj.hasOwnProperty('completed_date')) {
        this.completed_date = initObj.completed_date
      }
      else {
        this.completed_date = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('compl_time')) {
        this.compl_time = initObj.compl_time
      }
      else {
        this.compl_time = '';
      }
      if (initObj.hasOwnProperty('route')) {
        this.route = initObj.route
      }
      else {
        this.route = [];
      }
      if (initObj.hasOwnProperty('split_attribute1')) {
        this.split_attribute1 = initObj.split_attribute1
      }
      else {
        this.split_attribute1 = '';
      }
      if (initObj.hasOwnProperty('split1')) {
        this.split1 = initObj.split1
      }
      else {
        this.split1 = 0.0;
      }
      if (initObj.hasOwnProperty('split_attribute2')) {
        this.split_attribute2 = initObj.split_attribute2
      }
      else {
        this.split_attribute2 = '';
      }
      if (initObj.hasOwnProperty('split2')) {
        this.split2 = initObj.split2
      }
      else {
        this.split2 = 0.0;
      }
      if (initObj.hasOwnProperty('split_attribute3')) {
        this.split_attribute3 = initObj.split_attribute3
      }
      else {
        this.split_attribute3 = '';
      }
      if (initObj.hasOwnProperty('split3')) {
        this.split3 = initObj.split3
      }
      else {
        this.split3 = 0.0;
      }
      if (initObj.hasOwnProperty('attribute2')) {
        this.attribute2 = initObj.attribute2
      }
      else {
        this.attribute2 = '';
      }
      if (initObj.hasOwnProperty('value2')) {
        this.value2 = initObj.value2
      }
      else {
        this.value2 = 0.0;
      }
      if (initObj.hasOwnProperty('attribute3')) {
        this.attribute3 = initObj.attribute3
      }
      else {
        this.attribute3 = '';
      }
      if (initObj.hasOwnProperty('value3')) {
        this.value3 = initObj.value3
      }
      else {
        this.value3 = 0.0;
      }
      if (initObj.hasOwnProperty('last_event')) {
        this.last_event = initObj.last_event
      }
      else {
        this.last_event = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type event
    // Serialize message field [generator_id]
    bufferOffset = _serializer.string(obj.generator_id, buffer, bufferOffset);
    // Serialize message field [ID]
    bufferOffset = _serializer.int32(obj.ID, buffer, bufferOffset);
    // Serialize message field [type]
    bufferOffset = _serializer.string(obj.type, buffer, bufferOffset);
    // Serialize message field [generation_date]
    bufferOffset = _serializer.time(obj.generation_date, buffer, bufferOffset);
    // Serialize message field [gen_time]
    bufferOffset = _serializer.string(obj.gen_time, buffer, bufferOffset);
    // Serialize message field [completed_date]
    bufferOffset = _serializer.time(obj.completed_date, buffer, bufferOffset);
    // Serialize message field [compl_time]
    bufferOffset = _serializer.string(obj.compl_time, buffer, bufferOffset);
    // Serialize message field [route]
    bufferOffset = _arraySerializer.string(obj.route, buffer, bufferOffset, null);
    // Serialize message field [split_attribute1]
    bufferOffset = _serializer.string(obj.split_attribute1, buffer, bufferOffset);
    // Serialize message field [split1]
    bufferOffset = _serializer.float32(obj.split1, buffer, bufferOffset);
    // Serialize message field [split_attribute2]
    bufferOffset = _serializer.string(obj.split_attribute2, buffer, bufferOffset);
    // Serialize message field [split2]
    bufferOffset = _serializer.float32(obj.split2, buffer, bufferOffset);
    // Serialize message field [split_attribute3]
    bufferOffset = _serializer.string(obj.split_attribute3, buffer, bufferOffset);
    // Serialize message field [split3]
    bufferOffset = _serializer.float32(obj.split3, buffer, bufferOffset);
    // Serialize message field [attribute2]
    bufferOffset = _serializer.string(obj.attribute2, buffer, bufferOffset);
    // Serialize message field [value2]
    bufferOffset = _serializer.float32(obj.value2, buffer, bufferOffset);
    // Serialize message field [attribute3]
    bufferOffset = _serializer.string(obj.attribute3, buffer, bufferOffset);
    // Serialize message field [value3]
    bufferOffset = _serializer.float32(obj.value3, buffer, bufferOffset);
    // Serialize message field [last_event]
    bufferOffset = _serializer.bool(obj.last_event, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type event
    let len;
    let data = new event(null);
    // Deserialize message field [generator_id]
    data.generator_id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [ID]
    data.ID = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [type]
    data.type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [generation_date]
    data.generation_date = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [gen_time]
    data.gen_time = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [completed_date]
    data.completed_date = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [compl_time]
    data.compl_time = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [route]
    data.route = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [split_attribute1]
    data.split_attribute1 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [split1]
    data.split1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [split_attribute2]
    data.split_attribute2 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [split2]
    data.split2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [split_attribute3]
    data.split_attribute3 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [split3]
    data.split3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [attribute2]
    data.attribute2 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [value2]
    data.value2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [attribute3]
    data.attribute3 = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [value3]
    data.value3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [last_event]
    data.last_event = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.generator_id);
    length += _getByteLength(object.type);
    length += _getByteLength(object.gen_time);
    length += _getByteLength(object.compl_time);
    object.route.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    length += _getByteLength(object.split_attribute1);
    length += _getByteLength(object.split_attribute2);
    length += _getByteLength(object.split_attribute3);
    length += _getByteLength(object.attribute2);
    length += _getByteLength(object.attribute3);
    return length + 81;
  }

  static datatype() {
    // Returns string type for a message object
    return 'simulator/event';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '11f9a94c34d2636c3fb0efd1e69990b4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new event(null);
    if (msg.generator_id !== undefined) {
      resolved.generator_id = msg.generator_id;
    }
    else {
      resolved.generator_id = ''
    }

    if (msg.ID !== undefined) {
      resolved.ID = msg.ID;
    }
    else {
      resolved.ID = 0
    }

    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = ''
    }

    if (msg.generation_date !== undefined) {
      resolved.generation_date = msg.generation_date;
    }
    else {
      resolved.generation_date = {secs: 0, nsecs: 0}
    }

    if (msg.gen_time !== undefined) {
      resolved.gen_time = msg.gen_time;
    }
    else {
      resolved.gen_time = ''
    }

    if (msg.completed_date !== undefined) {
      resolved.completed_date = msg.completed_date;
    }
    else {
      resolved.completed_date = {secs: 0, nsecs: 0}
    }

    if (msg.compl_time !== undefined) {
      resolved.compl_time = msg.compl_time;
    }
    else {
      resolved.compl_time = ''
    }

    if (msg.route !== undefined) {
      resolved.route = msg.route;
    }
    else {
      resolved.route = []
    }

    if (msg.split_attribute1 !== undefined) {
      resolved.split_attribute1 = msg.split_attribute1;
    }
    else {
      resolved.split_attribute1 = ''
    }

    if (msg.split1 !== undefined) {
      resolved.split1 = msg.split1;
    }
    else {
      resolved.split1 = 0.0
    }

    if (msg.split_attribute2 !== undefined) {
      resolved.split_attribute2 = msg.split_attribute2;
    }
    else {
      resolved.split_attribute2 = ''
    }

    if (msg.split2 !== undefined) {
      resolved.split2 = msg.split2;
    }
    else {
      resolved.split2 = 0.0
    }

    if (msg.split_attribute3 !== undefined) {
      resolved.split_attribute3 = msg.split_attribute3;
    }
    else {
      resolved.split_attribute3 = ''
    }

    if (msg.split3 !== undefined) {
      resolved.split3 = msg.split3;
    }
    else {
      resolved.split3 = 0.0
    }

    if (msg.attribute2 !== undefined) {
      resolved.attribute2 = msg.attribute2;
    }
    else {
      resolved.attribute2 = ''
    }

    if (msg.value2 !== undefined) {
      resolved.value2 = msg.value2;
    }
    else {
      resolved.value2 = 0.0
    }

    if (msg.attribute3 !== undefined) {
      resolved.attribute3 = msg.attribute3;
    }
    else {
      resolved.attribute3 = ''
    }

    if (msg.value3 !== undefined) {
      resolved.value3 = msg.value3;
    }
    else {
      resolved.value3 = 0.0
    }

    if (msg.last_event !== undefined) {
      resolved.last_event = msg.last_event;
    }
    else {
      resolved.last_event = false
    }

    return resolved;
    }
};

module.exports = event;
