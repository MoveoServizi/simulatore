;; Auto-generated. Do not edit!


(when (boundp 'simulator::cluster)
  (if (not (find-package "SIMULATOR"))
    (make-package "SIMULATOR"))
  (shadow 'cluster (find-package "SIMULATOR")))
(unless (find-package "SIMULATOR::CLUSTER")
  (make-package "SIMULATOR::CLUSTER"))

(in-package "ROS")
;;//! \htmlinclude cluster.msg.html


(defclass simulator::cluster
  :super ros::object
  :slots (_cluster_id _size _events ))

(defmethod simulator::cluster
  (:init
   (&key
    ((:cluster_id __cluster_id) 0)
    ((:size __size) 0)
    ((:events __events) ())
    )
   (send-super :init)
   (setq _cluster_id (round __cluster_id))
   (setq _size (round __size))
   (setq _events __events)
   self)
  (:cluster_id
   (&optional __cluster_id)
   (if __cluster_id (setq _cluster_id __cluster_id)) _cluster_id)
  (:size
   (&optional __size)
   (if __size (setq _size __size)) _size)
  (:events
   (&rest __events)
   (if (keywordp (car __events))
       (send* _events __events)
     (progn
       (if __events (setq _events (car __events)))
       _events)))
  (:serialization-length
   ()
   (+
    ;; int32 _cluster_id
    4
    ;; int32 _size
    4
    ;; simulator/event[] _events
    (apply #'+ (send-all _events :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _cluster_id
       (write-long _cluster_id s)
     ;; int32 _size
       (write-long _size s)
     ;; simulator/event[] _events
     (write-long (length _events) s)
     (dolist (elem _events)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _cluster_id
     (setq _cluster_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _size
     (setq _size (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; simulator/event[] _events
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _events (let (r) (dotimes (i n) (push (instance simulator::event :init) r)) r))
     (dolist (elem- _events)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get simulator::cluster :md5sum-) "be8d7800e24ef3d0dd2a228257781b9f")
(setf (get simulator::cluster :datatype-) "simulator/cluster")
(setf (get simulator::cluster :definition-)
      "int32 cluster_id
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





")



(provide :simulator/cluster "be8d7800e24ef3d0dd2a228257781b9f")


