;; Auto-generated. Do not edit!


(when (boundp 'simulator::loginfo)
  (if (not (find-package "SIMULATOR"))
    (make-package "SIMULATOR"))
  (shadow 'loginfo (find-package "SIMULATOR")))
(unless (find-package "SIMULATOR::LOGINFO")
  (make-package "SIMULATOR::LOGINFO"))

(in-package "ROS")
;;//! \htmlinclude loginfo.msg.html


(defclass simulator::loginfo
  :super ros::object
  :slots (_ID_node _type _node_name _utiliz_tot _utiliz_array _queue_array _time_array _info _queue_left _events_left _stop_esecution _statistic ))

(defmethod simulator::loginfo
  (:init
   (&key
    ((:ID_node __ID_node) 0)
    ((:type __type) "")
    ((:node_name __node_name) "")
    ((:utiliz_tot __utiliz_tot) 0.0)
    ((:utiliz_array __utiliz_array) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:queue_array __queue_array) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:time_array __time_array) (let (r) (dotimes (i 0) (push (instance ros::time :init) r)) r))
    ((:info __info) "")
    ((:queue_left __queue_left) 0)
    ((:events_left __events_left) 0)
    ((:stop_esecution __stop_esecution) nil)
    ((:statistic __statistic) nil)
    )
   (send-super :init)
   (setq _ID_node (round __ID_node))
   (setq _type (string __type))
   (setq _node_name (string __node_name))
   (setq _utiliz_tot (float __utiliz_tot))
   (setq _utiliz_array __utiliz_array)
   (setq _queue_array __queue_array)
   (setq _time_array __time_array)
   (setq _info (string __info))
   (setq _queue_left (round __queue_left))
   (setq _events_left (round __events_left))
   (setq _stop_esecution __stop_esecution)
   (setq _statistic __statistic)
   self)
  (:ID_node
   (&optional __ID_node)
   (if __ID_node (setq _ID_node __ID_node)) _ID_node)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:node_name
   (&optional __node_name)
   (if __node_name (setq _node_name __node_name)) _node_name)
  (:utiliz_tot
   (&optional __utiliz_tot)
   (if __utiliz_tot (setq _utiliz_tot __utiliz_tot)) _utiliz_tot)
  (:utiliz_array
   (&optional __utiliz_array)
   (if __utiliz_array (setq _utiliz_array __utiliz_array)) _utiliz_array)
  (:queue_array
   (&optional __queue_array)
   (if __queue_array (setq _queue_array __queue_array)) _queue_array)
  (:time_array
   (&optional __time_array)
   (if __time_array (setq _time_array __time_array)) _time_array)
  (:info
   (&optional __info)
   (if __info (setq _info __info)) _info)
  (:queue_left
   (&optional __queue_left)
   (if __queue_left (setq _queue_left __queue_left)) _queue_left)
  (:events_left
   (&optional __events_left)
   (if __events_left (setq _events_left __events_left)) _events_left)
  (:stop_esecution
   (&optional (__stop_esecution :null))
   (if (not (eq __stop_esecution :null)) (setq _stop_esecution __stop_esecution)) _stop_esecution)
  (:statistic
   (&optional (__statistic :null))
   (if (not (eq __statistic :null)) (setq _statistic __statistic)) _statistic)
  (:serialization-length
   ()
   (+
    ;; int32 _ID_node
    4
    ;; string _type
    4 (length _type)
    ;; string _node_name
    4 (length _node_name)
    ;; float32 _utiliz_tot
    4
    ;; float32[] _utiliz_array
    (* 4    (length _utiliz_array)) 4
    ;; float32[] _queue_array
    (* 4    (length _queue_array)) 4
    ;; time[] _time_array
    (* 8    (length _time_array)) 4
    ;; string _info
    4 (length _info)
    ;; int32 _queue_left
    4
    ;; int32 _events_left
    4
    ;; bool _stop_esecution
    1
    ;; bool _statistic
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _ID_node
       (write-long _ID_node s)
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; string _node_name
       (write-long (length _node_name) s) (princ _node_name s)
     ;; float32 _utiliz_tot
       (sys::poke _utiliz_tot (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32[] _utiliz_array
     (write-long (length _utiliz_array) s)
     (dotimes (i (length _utiliz_array))
       (sys::poke (elt _utiliz_array i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _queue_array
     (write-long (length _queue_array) s)
     (dotimes (i (length _queue_array))
       (sys::poke (elt _queue_array i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; time[] _time_array
     (write-long (length _time_array) s)
     (dotimes (i (length _time_array))
       (write-long (send (elt _time_array i) :sec) s) (write-long (send (elt _time_array i) :nsec) s)
       )
     ;; string _info
       (write-long (length _info) s) (princ _info s)
     ;; int32 _queue_left
       (write-long _queue_left s)
     ;; int32 _events_left
       (write-long _events_left s)
     ;; bool _stop_esecution
       (if _stop_esecution (write-byte -1 s) (write-byte 0 s))
     ;; bool _statistic
       (if _statistic (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _ID_node
     (setq _ID_node (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _node_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _node_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _utiliz_tot
     (setq _utiliz_tot (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32[] _utiliz_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _utiliz_array (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _utiliz_array i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _queue_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _queue_array (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _queue_array i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; time[] _time_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _time_array (let (r) (dotimes (i n) (push (instance ros::time :init) r)) r))
     (dolist (elem- _time_array)
     (send elem- :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send elem- :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; string _info
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _info (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _queue_left
     (setq _queue_left (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _events_left
     (setq _events_left (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _stop_esecution
     (setq _stop_esecution (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _statistic
     (setq _statistic (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get simulator::loginfo :md5sum-) "a5ab383abb11907064bb91db32d4aea1")
(setf (get simulator::loginfo :datatype-) "simulator/loginfo")
(setf (get simulator::loginfo :definition-)
      "int32 ID_node
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
bool statistic
")



(provide :simulator/loginfo "a5ab383abb11907064bb91db32d4aea1")

