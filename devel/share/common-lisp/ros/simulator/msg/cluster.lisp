; Auto-generated. Do not edit!


(cl:in-package simulator-msg)


;//! \htmlinclude cluster.msg.html

(cl:defclass <cluster> (roslisp-msg-protocol:ros-message)
  ((cluster_id
    :reader cluster_id
    :initarg :cluster_id
    :type cl:integer
    :initform 0)
   (size
    :reader size
    :initarg :size
    :type cl:integer
    :initform 0)
   (events
    :reader events
    :initarg :events
    :type (cl:vector simulator-msg:event)
   :initform (cl:make-array 0 :element-type 'simulator-msg:event :initial-element (cl:make-instance 'simulator-msg:event))))
)

(cl:defclass cluster (<cluster>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <cluster>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'cluster)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name simulator-msg:<cluster> is deprecated: use simulator-msg:cluster instead.")))

(cl:ensure-generic-function 'cluster_id-val :lambda-list '(m))
(cl:defmethod cluster_id-val ((m <cluster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:cluster_id-val is deprecated.  Use simulator-msg:cluster_id instead.")
  (cluster_id m))

(cl:ensure-generic-function 'size-val :lambda-list '(m))
(cl:defmethod size-val ((m <cluster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:size-val is deprecated.  Use simulator-msg:size instead.")
  (size m))

(cl:ensure-generic-function 'events-val :lambda-list '(m))
(cl:defmethod events-val ((m <cluster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:events-val is deprecated.  Use simulator-msg:events instead.")
  (events m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <cluster>) ostream)
  "Serializes a message object of type '<cluster>"
  (cl:let* ((signed (cl:slot-value msg 'cluster_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'size)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'events))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'events))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <cluster>) istream)
  "Deserializes a message object of type '<cluster>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cluster_id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'size) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'events) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'events)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'simulator-msg:event))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<cluster>)))
  "Returns string type for a message object of type '<cluster>"
  "simulator/cluster")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'cluster)))
  "Returns string type for a message object of type 'cluster"
  "simulator/cluster")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<cluster>)))
  "Returns md5sum for a message object of type '<cluster>"
  "be8d7800e24ef3d0dd2a228257781b9f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'cluster)))
  "Returns md5sum for a message object of type 'cluster"
  "be8d7800e24ef3d0dd2a228257781b9f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<cluster>)))
  "Returns full string definition for message of type '<cluster>"
  (cl:format cl:nil "int32 cluster_id~%int32 size~%event[] events~%================================================================================~%MSG: simulator/event~%string generator_id~%int32 ID~%string type~%time generation_date~%string gen_time~%time completed_date~%string compl_time~%string[] route~%string split_attribute1~%float32 split1~%string split_attribute2~%float32 split2~%string split_attribute3~%float32 split3~%string attribute2~%float32 value2~%string attribute3~%float32 value3~%bool last_event~%bool first_event~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'cluster)))
  "Returns full string definition for message of type 'cluster"
  (cl:format cl:nil "int32 cluster_id~%int32 size~%event[] events~%================================================================================~%MSG: simulator/event~%string generator_id~%int32 ID~%string type~%time generation_date~%string gen_time~%time completed_date~%string compl_time~%string[] route~%string split_attribute1~%float32 split1~%string split_attribute2~%float32 split2~%string split_attribute3~%float32 split3~%string attribute2~%float32 value2~%string attribute3~%float32 value3~%bool last_event~%bool first_event~%~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <cluster>))
  (cl:+ 0
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'events) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <cluster>))
  "Converts a ROS message object to a list"
  (cl:list 'cluster
    (cl:cons ':cluster_id (cluster_id msg))
    (cl:cons ':size (size msg))
    (cl:cons ':events (events msg))
))
