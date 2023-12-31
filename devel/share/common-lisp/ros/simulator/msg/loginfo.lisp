; Auto-generated. Do not edit!


(cl:in-package simulator-msg)


;//! \htmlinclude loginfo.msg.html

(cl:defclass <loginfo> (roslisp-msg-protocol:ros-message)
  ((ID_node
    :reader ID_node
    :initarg :ID_node
    :type cl:integer
    :initform 0)
   (type
    :reader type
    :initarg :type
    :type cl:string
    :initform "")
   (node_name
    :reader node_name
    :initarg :node_name
    :type cl:string
    :initform "")
   (server_time
    :reader server_time
    :initarg :server_time
    :type cl:float
    :initform 0.0)
   (num_servers
    :reader num_servers
    :initarg :num_servers
    :type cl:float
    :initform 0.0)
   (utiliz_tot
    :reader utiliz_tot
    :initarg :utiliz_tot
    :type cl:float
    :initform 0.0)
   (utiliz_array
    :reader utiliz_array
    :initarg :utiliz_array
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (utiliz_array_tot
    :reader utiliz_array_tot
    :initarg :utiliz_array_tot
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (queue_array
    :reader queue_array
    :initarg :queue_array
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (time_array
    :reader time_array
    :initarg :time_array
    :type (cl:vector cl:real)
   :initform (cl:make-array 0 :element-type 'cl:real :initial-element 0))
   (time_array_intervals
    :reader time_array_intervals
    :initarg :time_array_intervals
    :type (cl:vector cl:real)
   :initform (cl:make-array 0 :element-type 'cl:real :initial-element 0))
   (queue_left
    :reader queue_left
    :initarg :queue_left
    :type cl:integer
    :initform 0)
   (event_processed
    :reader event_processed
    :initarg :event_processed
    :type cl:integer
    :initform 0)
   (info
    :reader info
    :initarg :info
    :type cl:string
    :initform "")
   (ready
    :reader ready
    :initarg :ready
    :type cl:boolean
    :initform cl:nil)
   (events_left
    :reader events_left
    :initarg :events_left
    :type cl:integer
    :initform 0)
   (start
    :reader start
    :initarg :start
    :type cl:real
    :initform 0)
   (start_esecution
    :reader start_esecution
    :initarg :start_esecution
    :type cl:boolean
    :initform cl:nil)
   (stop_esecution
    :reader stop_esecution
    :initarg :stop_esecution
    :type cl:boolean
    :initform cl:nil)
   (statistic
    :reader statistic
    :initarg :statistic
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass loginfo (<loginfo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <loginfo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'loginfo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name simulator-msg:<loginfo> is deprecated: use simulator-msg:loginfo instead.")))

(cl:ensure-generic-function 'ID_node-val :lambda-list '(m))
(cl:defmethod ID_node-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:ID_node-val is deprecated.  Use simulator-msg:ID_node instead.")
  (ID_node m))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:type-val is deprecated.  Use simulator-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'node_name-val :lambda-list '(m))
(cl:defmethod node_name-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:node_name-val is deprecated.  Use simulator-msg:node_name instead.")
  (node_name m))

(cl:ensure-generic-function 'server_time-val :lambda-list '(m))
(cl:defmethod server_time-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:server_time-val is deprecated.  Use simulator-msg:server_time instead.")
  (server_time m))

(cl:ensure-generic-function 'num_servers-val :lambda-list '(m))
(cl:defmethod num_servers-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:num_servers-val is deprecated.  Use simulator-msg:num_servers instead.")
  (num_servers m))

(cl:ensure-generic-function 'utiliz_tot-val :lambda-list '(m))
(cl:defmethod utiliz_tot-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:utiliz_tot-val is deprecated.  Use simulator-msg:utiliz_tot instead.")
  (utiliz_tot m))

(cl:ensure-generic-function 'utiliz_array-val :lambda-list '(m))
(cl:defmethod utiliz_array-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:utiliz_array-val is deprecated.  Use simulator-msg:utiliz_array instead.")
  (utiliz_array m))

(cl:ensure-generic-function 'utiliz_array_tot-val :lambda-list '(m))
(cl:defmethod utiliz_array_tot-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:utiliz_array_tot-val is deprecated.  Use simulator-msg:utiliz_array_tot instead.")
  (utiliz_array_tot m))

(cl:ensure-generic-function 'queue_array-val :lambda-list '(m))
(cl:defmethod queue_array-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:queue_array-val is deprecated.  Use simulator-msg:queue_array instead.")
  (queue_array m))

(cl:ensure-generic-function 'time_array-val :lambda-list '(m))
(cl:defmethod time_array-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:time_array-val is deprecated.  Use simulator-msg:time_array instead.")
  (time_array m))

(cl:ensure-generic-function 'time_array_intervals-val :lambda-list '(m))
(cl:defmethod time_array_intervals-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:time_array_intervals-val is deprecated.  Use simulator-msg:time_array_intervals instead.")
  (time_array_intervals m))

(cl:ensure-generic-function 'queue_left-val :lambda-list '(m))
(cl:defmethod queue_left-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:queue_left-val is deprecated.  Use simulator-msg:queue_left instead.")
  (queue_left m))

(cl:ensure-generic-function 'event_processed-val :lambda-list '(m))
(cl:defmethod event_processed-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:event_processed-val is deprecated.  Use simulator-msg:event_processed instead.")
  (event_processed m))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:info-val is deprecated.  Use simulator-msg:info instead.")
  (info m))

(cl:ensure-generic-function 'ready-val :lambda-list '(m))
(cl:defmethod ready-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:ready-val is deprecated.  Use simulator-msg:ready instead.")
  (ready m))

(cl:ensure-generic-function 'events_left-val :lambda-list '(m))
(cl:defmethod events_left-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:events_left-val is deprecated.  Use simulator-msg:events_left instead.")
  (events_left m))

(cl:ensure-generic-function 'start-val :lambda-list '(m))
(cl:defmethod start-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:start-val is deprecated.  Use simulator-msg:start instead.")
  (start m))

(cl:ensure-generic-function 'start_esecution-val :lambda-list '(m))
(cl:defmethod start_esecution-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:start_esecution-val is deprecated.  Use simulator-msg:start_esecution instead.")
  (start_esecution m))

(cl:ensure-generic-function 'stop_esecution-val :lambda-list '(m))
(cl:defmethod stop_esecution-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:stop_esecution-val is deprecated.  Use simulator-msg:stop_esecution instead.")
  (stop_esecution m))

(cl:ensure-generic-function 'statistic-val :lambda-list '(m))
(cl:defmethod statistic-val ((m <loginfo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:statistic-val is deprecated.  Use simulator-msg:statistic instead.")
  (statistic m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <loginfo>) ostream)
  "Serializes a message object of type '<loginfo>"
  (cl:let* ((signed (cl:slot-value msg 'ID_node)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'type))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'node_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'node_name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'server_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'num_servers))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'utiliz_tot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'utiliz_array))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'utiliz_array))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'utiliz_array_tot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'utiliz_array_tot))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'queue_array))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'queue_array))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'time_array))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__sec (cl:floor ele))
        (__nsec (cl:round (cl:* 1e9 (cl:- ele (cl:floor ele))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream)))
   (cl:slot-value msg 'time_array))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'time_array_intervals))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__sec (cl:floor ele))
        (__nsec (cl:round (cl:* 1e9 (cl:- ele (cl:floor ele))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream)))
   (cl:slot-value msg 'time_array_intervals))
  (cl:let* ((signed (cl:slot-value msg 'queue_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'event_processed)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'info))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ready) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'events_left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'start)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'start) (cl:floor (cl:slot-value msg 'start)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'start_esecution) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'stop_esecution) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'statistic) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <loginfo>) istream)
  "Deserializes a message object of type '<loginfo>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ID_node) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'node_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'node_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'server_time) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'num_servers) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'utiliz_tot) (roslisp-utils:decode-single-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'utiliz_array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'utiliz_array)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'utiliz_array_tot) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'utiliz_array_tot)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'queue_array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'queue_array)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'time_array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'time_array)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'time_array_intervals) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'time_array_intervals)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9)))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'queue_left) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'event_processed) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'info) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'info) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'ready) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'events_left) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'start) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:setf (cl:slot-value msg 'start_esecution) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'stop_esecution) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'statistic) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<loginfo>)))
  "Returns string type for a message object of type '<loginfo>"
  "simulator/loginfo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'loginfo)))
  "Returns string type for a message object of type 'loginfo"
  "simulator/loginfo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<loginfo>)))
  "Returns md5sum for a message object of type '<loginfo>"
  "55d87199e7f17ce94759f154f0e8ee23")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'loginfo)))
  "Returns md5sum for a message object of type 'loginfo"
  "55d87199e7f17ce94759f154f0e8ee23")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<loginfo>)))
  "Returns full string definition for message of type '<loginfo>"
  (cl:format cl:nil "int32 ID_node~%string type~%string node_name~%~%float32 server_time~%float32 num_servers~%float32 utiliz_tot~%float32[] utiliz_array~%float32[] utiliz_array_tot~%float32[] queue_array~%time[] time_array~%time[] time_array_intervals~%int32 queue_left~%int32 event_processed~%string info~%bool ready~%~%int32 events_left~%time start~%~%bool start_esecution~%bool stop_esecution~%bool statistic~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'loginfo)))
  "Returns full string definition for message of type 'loginfo"
  (cl:format cl:nil "int32 ID_node~%string type~%string node_name~%~%float32 server_time~%float32 num_servers~%float32 utiliz_tot~%float32[] utiliz_array~%float32[] utiliz_array_tot~%float32[] queue_array~%time[] time_array~%time[] time_array_intervals~%int32 queue_left~%int32 event_processed~%string info~%bool ready~%~%int32 events_left~%time start~%~%bool start_esecution~%bool stop_esecution~%bool statistic~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <loginfo>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'type))
     4 (cl:length (cl:slot-value msg 'node_name))
     4
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'utiliz_array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'utiliz_array_tot) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'queue_array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'time_array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'time_array_intervals) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4
     4
     4 (cl:length (cl:slot-value msg 'info))
     1
     4
     8
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <loginfo>))
  "Converts a ROS message object to a list"
  (cl:list 'loginfo
    (cl:cons ':ID_node (ID_node msg))
    (cl:cons ':type (type msg))
    (cl:cons ':node_name (node_name msg))
    (cl:cons ':server_time (server_time msg))
    (cl:cons ':num_servers (num_servers msg))
    (cl:cons ':utiliz_tot (utiliz_tot msg))
    (cl:cons ':utiliz_array (utiliz_array msg))
    (cl:cons ':utiliz_array_tot (utiliz_array_tot msg))
    (cl:cons ':queue_array (queue_array msg))
    (cl:cons ':time_array (time_array msg))
    (cl:cons ':time_array_intervals (time_array_intervals msg))
    (cl:cons ':queue_left (queue_left msg))
    (cl:cons ':event_processed (event_processed msg))
    (cl:cons ':info (info msg))
    (cl:cons ':ready (ready msg))
    (cl:cons ':events_left (events_left msg))
    (cl:cons ':start (start msg))
    (cl:cons ':start_esecution (start_esecution msg))
    (cl:cons ':stop_esecution (stop_esecution msg))
    (cl:cons ':statistic (statistic msg))
))
