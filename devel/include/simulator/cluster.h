// Generated by gencpp from file simulator/cluster.msg
// DO NOT EDIT!


#ifndef SIMULATOR_MESSAGE_CLUSTER_H
#define SIMULATOR_MESSAGE_CLUSTER_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <simulator/event.h>

namespace simulator
{
template <class ContainerAllocator>
struct cluster_
{
  typedef cluster_<ContainerAllocator> Type;

  cluster_()
    : cluster_id(0)
    , size(0)
    , events()  {
    }
  cluster_(const ContainerAllocator& _alloc)
    : cluster_id(0)
    , size(0)
    , events(_alloc)  {
  (void)_alloc;
    }



   typedef int32_t _cluster_id_type;
  _cluster_id_type cluster_id;

   typedef int32_t _size_type;
  _size_type size;

   typedef std::vector< ::simulator::event_<ContainerAllocator> , typename std::allocator_traits<ContainerAllocator>::template rebind_alloc< ::simulator::event_<ContainerAllocator> >> _events_type;
  _events_type events;





  typedef boost::shared_ptr< ::simulator::cluster_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::simulator::cluster_<ContainerAllocator> const> ConstPtr;

}; // struct cluster_

typedef ::simulator::cluster_<std::allocator<void> > cluster;

typedef boost::shared_ptr< ::simulator::cluster > clusterPtr;
typedef boost::shared_ptr< ::simulator::cluster const> clusterConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::simulator::cluster_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::simulator::cluster_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::simulator::cluster_<ContainerAllocator1> & lhs, const ::simulator::cluster_<ContainerAllocator2> & rhs)
{
  return lhs.cluster_id == rhs.cluster_id &&
    lhs.size == rhs.size &&
    lhs.events == rhs.events;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::simulator::cluster_<ContainerAllocator1> & lhs, const ::simulator::cluster_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace simulator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::simulator::cluster_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::simulator::cluster_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::simulator::cluster_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::simulator::cluster_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simulator::cluster_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simulator::cluster_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::simulator::cluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "be8d7800e24ef3d0dd2a228257781b9f";
  }

  static const char* value(const ::simulator::cluster_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbe8d7800e24ef3d0ULL;
  static const uint64_t static_value2 = 0xdd2a228257781b9fULL;
};

template<class ContainerAllocator>
struct DataType< ::simulator::cluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "simulator/cluster";
  }

  static const char* value(const ::simulator::cluster_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::simulator::cluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 cluster_id\n"
"int32 size\n"
"event[] events\n"
"================================================================================\n"
"MSG: simulator/event\n"
"string generator_id\n"
"int32 ID\n"
"string type\n"
"time generation_date\n"
"string gen_time\n"
"time completed_date\n"
"string compl_time\n"
"string[] route\n"
"string split_attribute1\n"
"float32 split1\n"
"string split_attribute2\n"
"float32 split2\n"
"string split_attribute3\n"
"float32 split3\n"
"string attribute2\n"
"float32 value2\n"
"string attribute3\n"
"float32 value3\n"
"bool last_event\n"
"bool first_event\n"
"\n"
"\n"
"\n"
"\n"
;
  }

  static const char* value(const ::simulator::cluster_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::simulator::cluster_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.cluster_id);
      stream.next(m.size);
      stream.next(m.events);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct cluster_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::simulator::cluster_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::simulator::cluster_<ContainerAllocator>& v)
  {
    s << indent << "cluster_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.cluster_id);
    s << indent << "size: ";
    Printer<int32_t>::stream(s, indent + "  ", v.size);
    s << indent << "events[]" << std::endl;
    for (size_t i = 0; i < v.events.size(); ++i)
    {
      s << indent << "  events[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::simulator::event_<ContainerAllocator> >::stream(s, indent + "    ", v.events[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SIMULATOR_MESSAGE_CLUSTER_H