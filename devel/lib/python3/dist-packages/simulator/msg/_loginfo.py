# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from simulator/loginfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class loginfo(genpy.Message):
  _md5sum = "55d87199e7f17ce94759f154f0e8ee23"
  _type = "simulator/loginfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 ID_node
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
bool statistic"""
  __slots__ = ['ID_node','type','node_name','server_time','num_servers','utiliz_tot','utiliz_array','utiliz_array_tot','queue_array','time_array','time_array_intervals','queue_left','event_processed','info','ready','events_left','start','start_esecution','stop_esecution','statistic']
  _slot_types = ['int32','string','string','float32','float32','float32','float32[]','float32[]','float32[]','time[]','time[]','int32','int32','string','bool','int32','time','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ID_node,type,node_name,server_time,num_servers,utiliz_tot,utiliz_array,utiliz_array_tot,queue_array,time_array,time_array_intervals,queue_left,event_processed,info,ready,events_left,start,start_esecution,stop_esecution,statistic

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
      if self.server_time is None:
        self.server_time = 0.
      if self.num_servers is None:
        self.num_servers = 0.
      if self.utiliz_tot is None:
        self.utiliz_tot = 0.
      if self.utiliz_array is None:
        self.utiliz_array = []
      if self.utiliz_array_tot is None:
        self.utiliz_array_tot = []
      if self.queue_array is None:
        self.queue_array = []
      if self.time_array is None:
        self.time_array = []
      if self.time_array_intervals is None:
        self.time_array_intervals = []
      if self.queue_left is None:
        self.queue_left = 0
      if self.event_processed is None:
        self.event_processed = 0
      if self.info is None:
        self.info = ''
      if self.ready is None:
        self.ready = False
      if self.events_left is None:
        self.events_left = 0
      if self.start is None:
        self.start = genpy.Time()
      if self.start_esecution is None:
        self.start_esecution = False
      if self.stop_esecution is None:
        self.stop_esecution = False
      if self.statistic is None:
        self.statistic = False
    else:
      self.ID_node = 0
      self.type = ''
      self.node_name = ''
      self.server_time = 0.
      self.num_servers = 0.
      self.utiliz_tot = 0.
      self.utiliz_array = []
      self.utiliz_array_tot = []
      self.queue_array = []
      self.time_array = []
      self.time_array_intervals = []
      self.queue_left = 0
      self.event_processed = 0
      self.info = ''
      self.ready = False
      self.events_left = 0
      self.start = genpy.Time()
      self.start_esecution = False
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
      _x = self
      buff.write(_get_struct_3f().pack(_x.server_time, _x.num_servers, _x.utiliz_tot))
      length = len(self.utiliz_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.utiliz_array))
      length = len(self.utiliz_array_tot)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.utiliz_array_tot))
      length = len(self.queue_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.queue_array))
      length = len(self.time_array)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_array:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
      length = len(self.time_array_intervals)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_array_intervals:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_get_struct_2i().pack(_x.queue_left, _x.event_processed))
      _x = self.info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_Bi2I3B().pack(_x.ready, _x.events_left, _x.start.secs, _x.start.nsecs, _x.start_esecution, _x.stop_esecution, _x.statistic))
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
      if self.time_array_intervals is None:
        self.time_array_intervals = None
      if self.start is None:
        self.start = genpy.Time()
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
      _x = self
      start = end
      end += 12
      (_x.server_time, _x.num_servers, _x.utiliz_tot,) = _get_struct_3f().unpack(str[start:end])
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
      self.utiliz_array_tot = s.unpack(str[start:end])
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
      self.time_array_intervals = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        self.time_array_intervals.append(val1)
      _x = self
      start = end
      end += 8
      (_x.queue_left, _x.event_processed,) = _get_struct_2i().unpack(str[start:end])
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
      end += 16
      (_x.ready, _x.events_left, _x.start.secs, _x.start.nsecs, _x.start_esecution, _x.stop_esecution, _x.statistic,) = _get_struct_Bi2I3B().unpack(str[start:end])
      self.ready = bool(self.ready)
      self.start_esecution = bool(self.start_esecution)
      self.stop_esecution = bool(self.stop_esecution)
      self.statistic = bool(self.statistic)
      self.start.canon()
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
      _x = self
      buff.write(_get_struct_3f().pack(_x.server_time, _x.num_servers, _x.utiliz_tot))
      length = len(self.utiliz_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.utiliz_array.tostring())
      length = len(self.utiliz_array_tot)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.utiliz_array_tot.tostring())
      length = len(self.queue_array)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.queue_array.tostring())
      length = len(self.time_array)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_array:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
      length = len(self.time_array_intervals)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_array_intervals:
        _x = val1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_get_struct_2i().pack(_x.queue_left, _x.event_processed))
      _x = self.info
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_Bi2I3B().pack(_x.ready, _x.events_left, _x.start.secs, _x.start.nsecs, _x.start_esecution, _x.stop_esecution, _x.statistic))
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
      if self.time_array_intervals is None:
        self.time_array_intervals = None
      if self.start is None:
        self.start = genpy.Time()
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
      _x = self
      start = end
      end += 12
      (_x.server_time, _x.num_servers, _x.utiliz_tot,) = _get_struct_3f().unpack(str[start:end])
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
      self.utiliz_array_tot = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
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
      self.time_array_intervals = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        self.time_array_intervals.append(val1)
      _x = self
      start = end
      end += 8
      (_x.queue_left, _x.event_processed,) = _get_struct_2i().unpack(str[start:end])
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
      end += 16
      (_x.ready, _x.events_left, _x.start.secs, _x.start.nsecs, _x.start_esecution, _x.stop_esecution, _x.statistic,) = _get_struct_Bi2I3B().unpack(str[start:end])
      self.ready = bool(self.ready)
      self.start_esecution = bool(self.start_esecution)
      self.stop_esecution = bool(self.stop_esecution)
      self.statistic = bool(self.statistic)
      self.start.canon()
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
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_Bi2I3B = None
def _get_struct_Bi2I3B():
    global _struct_Bi2I3B
    if _struct_Bi2I3B is None:
        _struct_Bi2I3B = struct.Struct("<Bi2I3B")
    return _struct_Bi2I3B
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
