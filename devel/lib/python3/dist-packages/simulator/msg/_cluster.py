# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from simulator/cluster.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import simulator.msg

class cluster(genpy.Message):
  _md5sum = "be8d7800e24ef3d0dd2a228257781b9f"
  _type = "simulator/cluster"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 cluster_id
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




"""
  __slots__ = ['cluster_id','size','events']
  _slot_types = ['int32','int32','simulator/event[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cluster_id,size,events

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(cluster, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cluster_id is None:
        self.cluster_id = 0
      if self.size is None:
        self.size = 0
      if self.events is None:
        self.events = []
    else:
      self.cluster_id = 0
      self.size = 0
      self.events = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2i().pack(_x.cluster_id, _x.size))
      length = len(self.events)
      buff.write(_struct_I.pack(length))
      for val1 in self.events:
        _x = val1.generator_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.ID
        buff.write(_get_struct_i().pack(_x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v1 = val1.generation_date
        _x = _v1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = val1.gen_time
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v2 = val1.completed_date
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = val1.compl_time
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.route)
        buff.write(_struct_I.pack(length))
        for val2 in val1.route:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1.split_attribute1
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.split1
        buff.write(_get_struct_f().pack(_x))
        _x = val1.split_attribute2
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.split2
        buff.write(_get_struct_f().pack(_x))
        _x = val1.split_attribute3
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.split3
        buff.write(_get_struct_f().pack(_x))
        _x = val1.attribute2
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.value2
        buff.write(_get_struct_f().pack(_x))
        _x = val1.attribute3
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_f2B().pack(_x.value3, _x.last_event, _x.first_event))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.events is None:
        self.events = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.cluster_id, _x.size,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.events = []
      for i in range(0, length):
        val1 = simulator.msg.event()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.generator_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.generator_id = str[start:end]
        start = end
        end += 4
        (val1.ID,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.type = str[start:end]
        _v3 = val1.generation_date
        _x = _v3
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.gen_time = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.gen_time = str[start:end]
        _v4 = val1.completed_date
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.compl_time = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.compl_time = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.route = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.route.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.split_attribute1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.split_attribute1 = str[start:end]
        start = end
        end += 4
        (val1.split1,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.split_attribute2 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.split_attribute2 = str[start:end]
        start = end
        end += 4
        (val1.split2,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.split_attribute3 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.split_attribute3 = str[start:end]
        start = end
        end += 4
        (val1.split3,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.attribute2 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.attribute2 = str[start:end]
        start = end
        end += 4
        (val1.value2,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.attribute3 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.attribute3 = str[start:end]
        _x = val1
        start = end
        end += 6
        (_x.value3, _x.last_event, _x.first_event,) = _get_struct_f2B().unpack(str[start:end])
        val1.last_event = bool(val1.last_event)
        val1.first_event = bool(val1.first_event)
        self.events.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2i().pack(_x.cluster_id, _x.size))
      length = len(self.events)
      buff.write(_struct_I.pack(length))
      for val1 in self.events:
        _x = val1.generator_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.ID
        buff.write(_get_struct_i().pack(_x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v5 = val1.generation_date
        _x = _v5
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = val1.gen_time
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v6 = val1.completed_date
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = val1.compl_time
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.route)
        buff.write(_struct_I.pack(length))
        for val2 in val1.route:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.Struct('<I%ss'%length).pack(length, val2))
        _x = val1.split_attribute1
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.split1
        buff.write(_get_struct_f().pack(_x))
        _x = val1.split_attribute2
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.split2
        buff.write(_get_struct_f().pack(_x))
        _x = val1.split_attribute3
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.split3
        buff.write(_get_struct_f().pack(_x))
        _x = val1.attribute2
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.value2
        buff.write(_get_struct_f().pack(_x))
        _x = val1.attribute3
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_f2B().pack(_x.value3, _x.last_event, _x.first_event))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.events is None:
        self.events = None
      end = 0
      _x = self
      start = end
      end += 8
      (_x.cluster_id, _x.size,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.events = []
      for i in range(0, length):
        val1 = simulator.msg.event()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.generator_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.generator_id = str[start:end]
        start = end
        end += 4
        (val1.ID,) = _get_struct_i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.type = str[start:end]
        _v7 = val1.generation_date
        _x = _v7
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.gen_time = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.gen_time = str[start:end]
        _v8 = val1.completed_date
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.compl_time = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.compl_time = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.route = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2 = str[start:end]
          val1.route.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.split_attribute1 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.split_attribute1 = str[start:end]
        start = end
        end += 4
        (val1.split1,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.split_attribute2 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.split_attribute2 = str[start:end]
        start = end
        end += 4
        (val1.split2,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.split_attribute3 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.split_attribute3 = str[start:end]
        start = end
        end += 4
        (val1.split3,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.attribute2 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.attribute2 = str[start:end]
        start = end
        end += 4
        (val1.value2,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.attribute3 = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.attribute3 = str[start:end]
        _x = val1
        start = end
        end += 6
        (_x.value3, _x.last_event, _x.first_event,) = _get_struct_f2B().unpack(str[start:end])
        val1.last_event = bool(val1.last_event)
        val1.first_event = bool(val1.first_event)
        self.events.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_f2B = None
def _get_struct_f2B():
    global _struct_f2B
    if _struct_f2B is None:
        _struct_f2B = struct.Struct("<f2B")
    return _struct_f2B
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
