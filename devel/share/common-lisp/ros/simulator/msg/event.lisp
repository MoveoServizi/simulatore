; Auto-generated. Do not edit!


(cl:in-package simulator-msg)


;//! \htmlinclude event.msg.html

(cl:defclass <event> (roslisp-msg-protocol:ros-message)
  ((generator_id
    :reader generator_id
    :initarg :generator_id
    :type cl:string
    :initform "")
   (ID
    :reader ID
    :initarg :ID
    :type cl:integer
    :initform 0)
   (type
    :reader type
    :initarg :type
    :type cl:string
    :initform "")
   (generation_date
    :reader generation_date
    :initarg :generation_date
    :type cl:real
    :initform 0)
   (gen_time
    :reader gen_time
    :initarg :gen_time
    :type cl:string
    :initform "")
   (completed_date
    :reader completed_date
    :initarg :completed_date
    :type cl:real
    :initform 0)
   (compl_time
    :reader compl_time
    :initarg :compl_time
    :type cl:string
    :initform "")
   (route
    :reader route
    :initarg :route
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (split_attribute1
    :reader split_attribute1
    :initarg :split_attribute1
    :type cl:string
    :initform "")
   (split1
    :reader split1
    :initarg :split1
    :type cl:float
    :initform 0.0)
   (split_attribute2
    :reader split_attribute2
    :initarg :split_attribute2
    :type cl:string
    :initform "")
   (split2
    :reader split2
    :initarg :split2
    :type cl:float
    :initform 0.0)
   (split_attribute3
    :reader split_attribute3
    :initarg :split_attribute3
    :type cl:string
    :initform "")
   (split3
    :reader split3
    :initarg :split3
    :type cl:float
    :initform 0.0)
   (attribute2
    :reader attribute2
    :initarg :attribute2
    :type cl:string
    :initform "")
   (value2
    :reader value2
    :initarg :value2
    :type cl:float
    :initform 0.0)
   (attribute3
    :reader attribute3
    :initarg :attribute3
    :type cl:string
    :initform "")
   (value3
    :reader value3
    :initarg :value3
    :type cl:float
    :initform 0.0)
   (last_event
    :reader last_event
    :initarg :last_event
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass event (<event>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <event>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'event)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name simulator-msg:<event> is deprecated: use simulator-msg:event instead.")))

(cl:ensure-generic-function 'generator_id-val :lambda-list '(m))
(cl:defmethod generator_id-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:generator_id-val is deprecated.  Use simulator-msg:generator_id instead.")
  (generator_id m))

(cl:ensure-generic-function 'ID-val :lambda-list '(m))
(cl:defmethod ID-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:ID-val is deprecated.  Use simulator-msg:ID instead.")
  (ID m))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:type-val is deprecated.  Use simulator-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'generation_date-val :lambda-list '(m))
(cl:defmethod generation_date-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:generation_date-val is deprecated.  Use simulator-msg:generation_date instead.")
  (generation_date m))

(cl:ensure-generic-function 'gen_time-val :lambda-list '(m))
(cl:defmethod gen_time-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:gen_time-val is deprecated.  Use simulator-msg:gen_time instead.")
  (gen_time m))

(cl:ensure-generic-function 'completed_date-val :lambda-list '(m))
(cl:defmethod completed_date-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:completed_date-val is deprecated.  Use simulator-msg:completed_date instead.")
  (completed_date m))

(cl:ensure-generic-function 'compl_time-val :lambda-list '(m))
(cl:defmethod compl_time-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:compl_time-val is deprecated.  Use simulator-msg:compl_time instead.")
  (compl_time m))

(cl:ensure-generic-function 'route-val :lambda-list '(m))
(cl:defmethod route-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:route-val is deprecated.  Use simulator-msg:route instead.")
  (route m))

(cl:ensure-generic-function 'split_attribute1-val :lambda-list '(m))
(cl:defmethod split_attribute1-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:split_attribute1-val is deprecated.  Use simulator-msg:split_attribute1 instead.")
  (split_attribute1 m))

(cl:ensure-generic-function 'split1-val :lambda-list '(m))
(cl:defmethod split1-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:split1-val is deprecated.  Use simulator-msg:split1 instead.")
  (split1 m))

(cl:ensure-generic-function 'split_attribute2-val :lambda-list '(m))
(cl:defmethod split_attribute2-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:split_attribute2-val is deprecated.  Use simulator-msg:split_attribute2 instead.")
  (split_attribute2 m))

(cl:ensure-generic-function 'split2-val :lambda-list '(m))
(cl:defmethod split2-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:split2-val is deprecated.  Use simulator-msg:split2 instead.")
  (split2 m))

(cl:ensure-generic-function 'split_attribute3-val :lambda-list '(m))
(cl:defmethod split_attribute3-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:split_attribute3-val is deprecated.  Use simulator-msg:split_attribute3 instead.")
  (split_attribute3 m))

(cl:ensure-generic-function 'split3-val :lambda-list '(m))
(cl:defmethod split3-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:split3-val is deprecated.  Use simulator-msg:split3 instead.")
  (split3 m))

(cl:ensure-generic-function 'attribute2-val :lambda-list '(m))
(cl:defmethod attribute2-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:attribute2-val is deprecated.  Use simulator-msg:attribute2 instead.")
  (attribute2 m))

(cl:ensure-generic-function 'value2-val :lambda-list '(m))
(cl:defmethod value2-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:value2-val is deprecated.  Use simulator-msg:value2 instead.")
  (value2 m))

(cl:ensure-generic-function 'attribute3-val :lambda-list '(m))
(cl:defmethod attribute3-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:attribute3-val is deprecated.  Use simulator-msg:attribute3 instead.")
  (attribute3 m))

(cl:ensure-generic-function 'value3-val :lambda-list '(m))
(cl:defmethod value3-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:value3-val is deprecated.  Use simulator-msg:value3 instead.")
  (value3 m))

(cl:ensure-generic-function 'last_event-val :lambda-list '(m))
(cl:defmethod last_event-val ((m <event>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simulator-msg:last_event-val is deprecated.  Use simulator-msg:last_event instead.")
  (last_event m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <event>) ostream)
  "Serializes a message object of type '<event>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'generator_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'generator_id))
  (cl:let* ((signed (cl:slot-value msg 'ID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
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
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'generation_date)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'generation_date) (cl:floor (cl:slot-value msg 'generation_date)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'gen_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'gen_time))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'completed_date)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'completed_date) (cl:floor (cl:slot-value msg 'completed_date)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'compl_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'compl_time))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'route))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'route))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'split_attribute1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'split_attribute1))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'split1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'split_attribute2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'split_attribute2))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'split2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'split_attribute3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'split_attribute3))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'split3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'attribute2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'attribute2))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'value2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'attribute3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'attribute3))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'value3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'last_event) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <event>) istream)
  "Deserializes a message object of type '<event>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'generator_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'generator_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ID) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'generation_date) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gen_time) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'gen_time) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'completed_date) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'compl_time) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'compl_time) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'route) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'route)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'split_attribute1) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'split_attribute1) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'split1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'split_attribute2) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'split_attribute2) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'split2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'split_attribute3) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'split_attribute3) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'split3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'attribute2) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'attribute2) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'value2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'attribute3) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'attribute3) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'value3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'last_event) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<event>)))
  "Returns string type for a message object of type '<event>"
  "simulator/event")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'event)))
  "Returns string type for a message object of type 'event"
  "simulator/event")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<event>)))
  "Returns md5sum for a message object of type '<event>"
  "11f9a94c34d2636c3fb0efd1e69990b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'event)))
  "Returns md5sum for a message object of type 'event"
  "11f9a94c34d2636c3fb0efd1e69990b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<event>)))
  "Returns full string definition for message of type '<event>"
  (cl:format cl:nil "string generator_id~%int32 ID~%string type~%time generation_date~%string gen_time~%time completed_date~%string compl_time~%string[] route~%string split_attribute1~%float32 split1~%string split_attribute2~%float32 split2~%string split_attribute3~%float32 split3~%~%string attribute2~%float32 value2~%string attribute3~%float32 value3~%~%~%bool last_event~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'event)))
  "Returns full string definition for message of type 'event"
  (cl:format cl:nil "string generator_id~%int32 ID~%string type~%time generation_date~%string gen_time~%time completed_date~%string compl_time~%string[] route~%string split_attribute1~%float32 split1~%string split_attribute2~%float32 split2~%string split_attribute3~%float32 split3~%~%string attribute2~%float32 value2~%string attribute3~%float32 value3~%~%~%bool last_event~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <event>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'generator_id))
     4
     4 (cl:length (cl:slot-value msg 'type))
     8
     4 (cl:length (cl:slot-value msg 'gen_time))
     8
     4 (cl:length (cl:slot-value msg 'compl_time))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'route) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:length (cl:slot-value msg 'split_attribute1))
     4
     4 (cl:length (cl:slot-value msg 'split_attribute2))
     4
     4 (cl:length (cl:slot-value msg 'split_attribute3))
     4
     4 (cl:length (cl:slot-value msg 'attribute2))
     4
     4 (cl:length (cl:slot-value msg 'attribute3))
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <event>))
  "Converts a ROS message object to a list"
  (cl:list 'event
    (cl:cons ':generator_id (generator_id msg))
    (cl:cons ':ID (ID msg))
    (cl:cons ':type (type msg))
    (cl:cons ':generation_date (generation_date msg))
    (cl:cons ':gen_time (gen_time msg))
    (cl:cons ':completed_date (completed_date msg))
    (cl:cons ':compl_time (compl_time msg))
    (cl:cons ':route (route msg))
    (cl:cons ':split_attribute1 (split_attribute1 msg))
    (cl:cons ':split1 (split1 msg))
    (cl:cons ':split_attribute2 (split_attribute2 msg))
    (cl:cons ':split2 (split2 msg))
    (cl:cons ':split_attribute3 (split_attribute3 msg))
    (cl:cons ':split3 (split3 msg))
    (cl:cons ':attribute2 (attribute2 msg))
    (cl:cons ':value2 (value2 msg))
    (cl:cons ':attribute3 (attribute3 msg))
    (cl:cons ':value3 (value3 msg))
    (cl:cons ':last_event (last_event msg))
))
