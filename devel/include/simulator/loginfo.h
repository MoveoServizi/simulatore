// Generated by gencpp from file simulator/loginfo.msg
// DO NOT EDIT!


#ifndef SIMULATOR_MESSAGE_LOGINFO_H
#define SIMULATOR_MESSAGE_LOGINFO_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace simulator
{
template <class ContainerAllocator>
struct loginfo_
{
  typedef loginfo_<ContainerAllocator> Type;

  loginfo_()
    : ID_node(0)
    , type()
    , node_name()
    , server_time(0.0)
    , num_servers(0.0)
    , utiliz_tot(0.0)
    , utiliz_array()
    , utiliz_array_tot()
    , queue_array()
    , time_array()
    , time_array_intervals()
    , queue_left(0)
    , event_processed(0)
    , info()
    , ready(false)
    , events_left(0)
    , start()
    , start_esecution(false)
    , stop_esecution(false)
    , statistic(false)  {
    }
  loginfo_(const ContainerAllocator& _alloc)
    : ID_node(0)
    , type(_alloc)
    , node_name(_alloc)
    , server_time(0.0)
    , num_servers(0.0)
    , utiliz_tot(0.0)
    , utiliz_array(_alloc)
    , utiliz_array_tot(_alloc)
    , queue_array(_alloc)
    , time_array(_alloc)
    , time_array_intervals(_alloc)
    , queue_left(0)
    , event_processed(0)
    , info(_alloc)
    , ready(false)
    , events_left(0)
    , start()
    , start_esecution(false)
    , stop_esecution(false)
    , statistic(false)  {
  (void)_alloc;
    }



   typedef int32_t _ID_node_type;
  _ID_node_type ID_node;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _type_type;
  _type_type type;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _node_name_type;
  _node_name_type node_name;

   typedef float _server_time_type;
  _server_time_type server_time;

   typedef float _num_servers_type;
  _num_servers_type num_servers;

   typedef float _utiliz_tot_type;
  _utiliz_tot_type utiliz_tot;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _utiliz_array_type;
  _utiliz_array_type utiliz_array;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _utiliz_array_tot_type;
  _utiliz_array_tot_type utiliz_array_tot;

   typedef std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> _queue_array_type;
  _queue_array_type queue_array;

   typedef std::vector<ros::Time, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<ros::Time>> _time_array_type;
  _time_array_type time_array;

   typedef std::vector<ros::Time, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<ros::Time>> _time_array_intervals_type;
  _time_array_intervals_type time_array_intervals;

   typedef int32_t _queue_left_type;
  _queue_left_type queue_left;

   typedef int32_t _event_processed_type;
  _event_processed_type event_processed;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _info_type;
  _info_type info;

   typedef uint8_t _ready_type;
  _ready_type ready;

   typedef int32_t _events_left_type;
  _events_left_type events_left;

   typedef ros::Time _start_type;
  _start_type start;

   typedef uint8_t _start_esecution_type;
  _start_esecution_type start_esecution;

   typedef uint8_t _stop_esecution_type;
  _stop_esecution_type stop_esecution;

   typedef uint8_t _statistic_type;
  _statistic_type statistic;





  typedef boost::shared_ptr< ::simulator::loginfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::simulator::loginfo_<ContainerAllocator> const> ConstPtr;

}; // struct loginfo_

typedef ::simulator::loginfo_<std::allocator<void> > loginfo;

typedef boost::shared_ptr< ::simulator::loginfo > loginfoPtr;
typedef boost::shared_ptr< ::simulator::loginfo const> loginfoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::simulator::loginfo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::simulator::loginfo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::simulator::loginfo_<ContainerAllocator1> & lhs, const ::simulator::loginfo_<ContainerAllocator2> & rhs)
{
  return lhs.ID_node == rhs.ID_node &&
    lhs.type == rhs.type &&
    lhs.node_name == rhs.node_name &&
    lhs.server_time == rhs.server_time &&
    lhs.num_servers == rhs.num_servers &&
    lhs.utiliz_tot == rhs.utiliz_tot &&
    lhs.utiliz_array == rhs.utiliz_array &&
    lhs.utiliz_array_tot == rhs.utiliz_array_tot &&
    lhs.queue_array == rhs.queue_array &&
    lhs.time_array == rhs.time_array &&
    lhs.time_array_intervals == rhs.time_array_intervals &&
    lhs.queue_left == rhs.queue_left &&
    lhs.event_processed == rhs.event_processed &&
    lhs.info == rhs.info &&
    lhs.ready == rhs.ready &&
    lhs.events_left == rhs.events_left &&
    lhs.start == rhs.start &&
    lhs.start_esecution == rhs.start_esecution &&
    lhs.stop_esecution == rhs.stop_esecution &&
    lhs.statistic == rhs.statistic;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::simulator::loginfo_<ContainerAllocator1> & lhs, const ::simulator::loginfo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace simulator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::simulator::loginfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::simulator::loginfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::simulator::loginfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::simulator::loginfo_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simulator::loginfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simulator::loginfo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::simulator::loginfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "55d87199e7f17ce94759f154f0e8ee23";
  }

  static const char* value(const ::simulator::loginfo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x55d87199e7f17ce9ULL;
  static const uint64_t static_value2 = 0x4759f154f0e8ee23ULL;
};

template<class ContainerAllocator>
struct DataType< ::simulator::loginfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "simulator/loginfo";
  }

  static const char* value(const ::simulator::loginfo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::simulator::loginfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 ID_node\n"
"string type\n"
"string node_name\n"
"\n"
"float32 server_time\n"
"float32 num_servers\n"
"float32 utiliz_tot\n"
"float32[] utiliz_array\n"
"float32[] utiliz_array_tot\n"
"float32[] queue_array\n"
"time[] time_array\n"
"time[] time_array_intervals\n"
"int32 queue_left\n"
"int32 event_processed\n"
"string info\n"
"bool ready\n"
"\n"
"int32 events_left\n"
"time start\n"
"\n"
"bool start_esecution\n"
"bool stop_esecution\n"
"bool statistic\n"
;
  }

  static const char* value(const ::simulator::loginfo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::simulator::loginfo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ID_node);
      stream.next(m.type);
      stream.next(m.node_name);
      stream.next(m.server_time);
      stream.next(m.num_servers);
      stream.next(m.utiliz_tot);
      stream.next(m.utiliz_array);
      stream.next(m.utiliz_array_tot);
      stream.next(m.queue_array);
      stream.next(m.time_array);
      stream.next(m.time_array_intervals);
      stream.next(m.queue_left);
      stream.next(m.event_processed);
      stream.next(m.info);
      stream.next(m.ready);
      stream.next(m.events_left);
      stream.next(m.start);
      stream.next(m.start_esecution);
      stream.next(m.stop_esecution);
      stream.next(m.statistic);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct loginfo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::simulator::loginfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::simulator::loginfo_<ContainerAllocator>& v)
  {
    s << indent << "ID_node: ";
    Printer<int32_t>::stream(s, indent + "  ", v.ID_node);
    s << indent << "type: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.type);
    s << indent << "node_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.node_name);
    s << indent << "server_time: ";
    Printer<float>::stream(s, indent + "  ", v.server_time);
    s << indent << "num_servers: ";
    Printer<float>::stream(s, indent + "  ", v.num_servers);
    s << indent << "utiliz_tot: ";
    Printer<float>::stream(s, indent + "  ", v.utiliz_tot);
    s << indent << "utiliz_array[]" << std::endl;
    for (size_t i = 0; i < v.utiliz_array.size(); ++i)
    {
      s << indent << "  utiliz_array[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.utiliz_array[i]);
    }
    s << indent << "utiliz_array_tot[]" << std::endl;
    for (size_t i = 0; i < v.utiliz_array_tot.size(); ++i)
    {
      s << indent << "  utiliz_array_tot[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.utiliz_array_tot[i]);
    }
    s << indent << "queue_array[]" << std::endl;
    for (size_t i = 0; i < v.queue_array.size(); ++i)
    {
      s << indent << "  queue_array[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.queue_array[i]);
    }
    s << indent << "time_array[]" << std::endl;
    for (size_t i = 0; i < v.time_array.size(); ++i)
    {
      s << indent << "  time_array[" << i << "]: ";
      Printer<ros::Time>::stream(s, indent + "  ", v.time_array[i]);
    }
    s << indent << "time_array_intervals[]" << std::endl;
    for (size_t i = 0; i < v.time_array_intervals.size(); ++i)
    {
      s << indent << "  time_array_intervals[" << i << "]: ";
      Printer<ros::Time>::stream(s, indent + "  ", v.time_array_intervals[i]);
    }
    s << indent << "queue_left: ";
    Printer<int32_t>::stream(s, indent + "  ", v.queue_left);
    s << indent << "event_processed: ";
    Printer<int32_t>::stream(s, indent + "  ", v.event_processed);
    s << indent << "info: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.info);
    s << indent << "ready: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ready);
    s << indent << "events_left: ";
    Printer<int32_t>::stream(s, indent + "  ", v.events_left);
    s << indent << "start: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.start);
    s << indent << "start_esecution: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.start_esecution);
    s << indent << "stop_esecution: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.stop_esecution);
    s << indent << "statistic: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.statistic);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SIMULATOR_MESSAGE_LOGINFO_H
