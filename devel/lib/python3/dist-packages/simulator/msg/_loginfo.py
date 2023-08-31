# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from simulator/loginfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class loginfo(genpy.Message):
  _md5sum = "a5ab383abb11907064bb91db32d4aea1"
  _type = "simulator/loginfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 ID_node
string type
string node_name

float32 utiliz_tot
float32[] utiliz_array
float32[] queue_array
time[] time_array
string info
int32 queue_left

int32 events_left

bool stop_esecution
bool statistic"""
  __slots__ = ['ID_node','type','node_name','utiliz_tot','utiliz_array','queue_array','time_array','info','queue_left','events_left','stop_esecution','statistic']
  _slot_types = ['int32','string','string','float32','float32[]','float32[]','time[]','string','int32','int32','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID_node,type,node_name,utiliz_tot,utiliz_array,queue_array,time_array,info,queue_left,events_left,stop_esecution,statistic

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(loginfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ID_node is None:
        self.ID_node = 0
      if self.type is None:
        self.type = ''
      if self.node_name is None:
        self.node_name = ''
      if self.utiliz_tot is None:
        self.utiliz_tot = 0.
      if self.utiliz_array is None:
        self.utiliz_array = []
      if self.queue_array is None:
        self.queue_array = []
      if self.time_array is None:
        self.time_array = []
      if self.info is None:
        self.info = ''
      if self.queue_left is None:
        self.queue_left = 0
      if self.events_left is None:
        self.events_left = 0
      if self.stop_esecution is None:
        self.stop_esecution = False
      if self.statistic is None:
        self.statistic = False
    else:
      self.ID_node = 0
      self.type = ''
      self.node_name = ''
      self.utiliz_tot = 0.
      self.utiliz_array = []
      self.queue_array = []
      self.time_array = []
      self.info = ''
      self.queue_left = 0
      self.events_left = 0
      self.stop_esecution = False
      self.statistic = False

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
      _x = self.ID_node
      buff.write(_get_struct_i().pack(_x))
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.node_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.utiliz_tot
      buff.write(_get_struct_f().pack(_x))
      length = len(self.utiliz_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.utiliz_array))
      length = len(self.queue_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.queue_array))
      length = len(self.time_array)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_array:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
      _x = self.info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i2B().pack(_x.queue_left, _x.events_left, _x.stop_esecution, _x.statistic))
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
      if self.time_array is None:
        self.time_array = None
      end = 0
      start = end
      end += 4
      (self.ID_node,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.node_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.node_name = str[start:end]
      start = end
      end += 4
      (self.utiliz_tot,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.utiliz_array = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.queue_array = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.time_array = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        self.time_array.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.info = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.info = str[start:end]
      _x = self
      start = end
      end += 10
      (_x.queue_left, _x.events_left, _x.stop_esecution, _x.statistic,) = _get_struct_2i2B().unpack(str[start:end])
      self.stop_esecution = bool(self.stop_esecution)
      self.statistic = bool(self.statistic)
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
      _x = self.ID_node
      buff.write(_get_struct_i().pack(_x))
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.node_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.utiliz_tot
      buff.write(_get_struct_f().pack(_x))
      length = len(self.utiliz_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.utiliz_array.tostring())
      length = len(self.queue_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.queue_array.tostring())
      length = len(self.time_array)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_array:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
      _x = self.info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2i2B().pack(_x.queue_left, _x.events_left, _x.stop_esecution, _x.statistic))
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
      if self.time_array is None:
        self.time_array = None
      end = 0
      start = end
      end += 4
      (self.ID_node,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.node_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.node_name = str[start:end]
      start = end
      end += 4
      (self.utiliz_tot,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.utiliz_array = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.queue_array = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.time_array = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        self.time_array.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.info = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.info = str[start:end]
      _x = self
      start = end
      end += 10
      (_x.queue_left, _x.events_left, _x.stop_esecution, _x.statistic,) = _get_struct_2i2B().unpack(str[start:end])
      self.stop_esecution = bool(self.stop_esecution)
      self.statistic = bool(self.statistic)
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
_struct_2i2B = None
def _get_struct_2i2B():
    global _struct_2i2B
    if _struct_2i2B is None:
        _struct_2i2B = struct.Struct("<2i2B")
    return _struct_2i2B
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i