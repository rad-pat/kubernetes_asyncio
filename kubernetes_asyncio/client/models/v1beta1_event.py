# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class V1beta1Event(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'api_version': 'str',
        'deprecated_count': 'int',
        'deprecated_first_timestamp': 'datetime',
        'deprecated_last_timestamp': 'datetime',
        'deprecated_source': 'V1EventSource',
        'event_time': 'datetime',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'note': 'str',
        'reason': 'str',
        'regarding': 'V1ObjectReference',
        'related': 'V1ObjectReference',
        'reporting_controller': 'str',
        'reporting_instance': 'str',
        'series': 'V1beta1EventSeries',
        'type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'api_version': 'apiVersion',
        'deprecated_count': 'deprecatedCount',
        'deprecated_first_timestamp': 'deprecatedFirstTimestamp',
        'deprecated_last_timestamp': 'deprecatedLastTimestamp',
        'deprecated_source': 'deprecatedSource',
        'event_time': 'eventTime',
        'kind': 'kind',
        'metadata': 'metadata',
        'note': 'note',
        'reason': 'reason',
        'regarding': 'regarding',
        'related': 'related',
        'reporting_controller': 'reportingController',
        'reporting_instance': 'reportingInstance',
        'series': 'series',
        'type': 'type'
    }

    def __init__(self, action=None, api_version=None, deprecated_count=None, deprecated_first_timestamp=None, deprecated_last_timestamp=None, deprecated_source=None, event_time=None, kind=None, metadata=None, note=None, reason=None, regarding=None, related=None, reporting_controller=None, reporting_instance=None, series=None, type=None):  # noqa: E501
        """V1beta1Event - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._api_version = None
        self._deprecated_count = None
        self._deprecated_first_timestamp = None
        self._deprecated_last_timestamp = None
        self._deprecated_source = None
        self._event_time = None
        self._kind = None
        self._metadata = None
        self._note = None
        self._reason = None
        self._regarding = None
        self._related = None
        self._reporting_controller = None
        self._reporting_instance = None
        self._series = None
        self._type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if api_version is not None:
            self.api_version = api_version
        if deprecated_count is not None:
            self.deprecated_count = deprecated_count
        if deprecated_first_timestamp is not None:
            self.deprecated_first_timestamp = deprecated_first_timestamp
        if deprecated_last_timestamp is not None:
            self.deprecated_last_timestamp = deprecated_last_timestamp
        if deprecated_source is not None:
            self.deprecated_source = deprecated_source
        self.event_time = event_time
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if note is not None:
            self.note = note
        if reason is not None:
            self.reason = reason
        if regarding is not None:
            self.regarding = regarding
        if related is not None:
            self.related = related
        if reporting_controller is not None:
            self.reporting_controller = reporting_controller
        if reporting_instance is not None:
            self.reporting_instance = reporting_instance
        if series is not None:
            self.series = series
        if type is not None:
            self.type = type

    @property
    def action(self):
        """Gets the action of this V1beta1Event.  # noqa: E501

        What action was taken/failed regarding to the regarding object.  # noqa: E501

        :return: The action of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1beta1Event.

        What action was taken/failed regarding to the regarding object.  # noqa: E501

        :param action: The action of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def api_version(self):
        """Gets the api_version of this V1beta1Event.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1beta1Event.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def deprecated_count(self):
        """Gets the deprecated_count of this V1beta1Event.  # noqa: E501

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :return: The deprecated_count of this V1beta1Event.  # noqa: E501
        :rtype: int
        """
        return self._deprecated_count

    @deprecated_count.setter
    def deprecated_count(self, deprecated_count):
        """Sets the deprecated_count of this V1beta1Event.

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :param deprecated_count: The deprecated_count of this V1beta1Event.  # noqa: E501
        :type: int
        """

        self._deprecated_count = deprecated_count

    @property
    def deprecated_first_timestamp(self):
        """Gets the deprecated_first_timestamp of this V1beta1Event.  # noqa: E501

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :return: The deprecated_first_timestamp of this V1beta1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._deprecated_first_timestamp

    @deprecated_first_timestamp.setter
    def deprecated_first_timestamp(self, deprecated_first_timestamp):
        """Sets the deprecated_first_timestamp of this V1beta1Event.

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :param deprecated_first_timestamp: The deprecated_first_timestamp of this V1beta1Event.  # noqa: E501
        :type: datetime
        """

        self._deprecated_first_timestamp = deprecated_first_timestamp

    @property
    def deprecated_last_timestamp(self):
        """Gets the deprecated_last_timestamp of this V1beta1Event.  # noqa: E501

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :return: The deprecated_last_timestamp of this V1beta1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._deprecated_last_timestamp

    @deprecated_last_timestamp.setter
    def deprecated_last_timestamp(self, deprecated_last_timestamp):
        """Sets the deprecated_last_timestamp of this V1beta1Event.

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :param deprecated_last_timestamp: The deprecated_last_timestamp of this V1beta1Event.  # noqa: E501
        :type: datetime
        """

        self._deprecated_last_timestamp = deprecated_last_timestamp

    @property
    def deprecated_source(self):
        """Gets the deprecated_source of this V1beta1Event.  # noqa: E501

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :return: The deprecated_source of this V1beta1Event.  # noqa: E501
        :rtype: V1EventSource
        """
        return self._deprecated_source

    @deprecated_source.setter
    def deprecated_source(self, deprecated_source):
        """Sets the deprecated_source of this V1beta1Event.

        Deprecated field assuring backward compatibility with core.v1 Event type  # noqa: E501

        :param deprecated_source: The deprecated_source of this V1beta1Event.  # noqa: E501
        :type: V1EventSource
        """

        self._deprecated_source = deprecated_source

    @property
    def event_time(self):
        """Gets the event_time of this V1beta1Event.  # noqa: E501

        Required. Time when this Event was first observed.  # noqa: E501

        :return: The event_time of this V1beta1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this V1beta1Event.

        Required. Time when this Event was first observed.  # noqa: E501

        :param event_time: The event_time of this V1beta1Event.  # noqa: E501
        :type: datetime
        """
        if event_time is None:
            raise ValueError("Invalid value for `event_time`, must not be `None`")  # noqa: E501

        self._event_time = event_time

    @property
    def kind(self):
        """Gets the kind of this V1beta1Event.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1Event.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1beta1Event.  # noqa: E501


        :return: The metadata of this V1beta1Event.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1beta1Event.


        :param metadata: The metadata of this V1beta1Event.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def note(self):
        """Gets the note of this V1beta1Event.  # noqa: E501

        Optional. A human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.  # noqa: E501

        :return: The note of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this V1beta1Event.

        Optional. A human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.  # noqa: E501

        :param note: The note of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def reason(self):
        """Gets the reason of this V1beta1Event.  # noqa: E501

        Why the action was taken.  # noqa: E501

        :return: The reason of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1beta1Event.

        Why the action was taken.  # noqa: E501

        :param reason: The reason of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def regarding(self):
        """Gets the regarding of this V1beta1Event.  # noqa: E501

        The object this Event is about. In most cases it's an Object reporting controller implements. E.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.  # noqa: E501

        :return: The regarding of this V1beta1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._regarding

    @regarding.setter
    def regarding(self, regarding):
        """Sets the regarding of this V1beta1Event.

        The object this Event is about. In most cases it's an Object reporting controller implements. E.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.  # noqa: E501

        :param regarding: The regarding of this V1beta1Event.  # noqa: E501
        :type: V1ObjectReference
        """

        self._regarding = regarding

    @property
    def related(self):
        """Gets the related of this V1beta1Event.  # noqa: E501

        Optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.  # noqa: E501

        :return: The related of this V1beta1Event.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this V1beta1Event.

        Optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.  # noqa: E501

        :param related: The related of this V1beta1Event.  # noqa: E501
        :type: V1ObjectReference
        """

        self._related = related

    @property
    def reporting_controller(self):
        """Gets the reporting_controller of this V1beta1Event.  # noqa: E501

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :return: The reporting_controller of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_controller

    @reporting_controller.setter
    def reporting_controller(self, reporting_controller):
        """Sets the reporting_controller of this V1beta1Event.

        Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.  # noqa: E501

        :param reporting_controller: The reporting_controller of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._reporting_controller = reporting_controller

    @property
    def reporting_instance(self):
        """Gets the reporting_instance of this V1beta1Event.  # noqa: E501

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :return: The reporting_instance of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._reporting_instance

    @reporting_instance.setter
    def reporting_instance(self, reporting_instance):
        """Sets the reporting_instance of this V1beta1Event.

        ID of the controller instance, e.g. `kubelet-xyzf`.  # noqa: E501

        :param reporting_instance: The reporting_instance of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._reporting_instance = reporting_instance

    @property
    def series(self):
        """Gets the series of this V1beta1Event.  # noqa: E501

        Data about the Event series this event represents or nil if it's a singleton Event.  # noqa: E501

        :return: The series of this V1beta1Event.  # noqa: E501
        :rtype: V1beta1EventSeries
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this V1beta1Event.

        Data about the Event series this event represents or nil if it's a singleton Event.  # noqa: E501

        :param series: The series of this V1beta1Event.  # noqa: E501
        :type: V1beta1EventSeries
        """

        self._series = series

    @property
    def type(self):
        """Gets the type of this V1beta1Event.  # noqa: E501

        Type of this event (Normal, Warning), new types could be added in the future.  # noqa: E501

        :return: The type of this V1beta1Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1beta1Event.

        Type of this event (Normal, Warning), new types could be added in the future.  # noqa: E501

        :param type: The type of this V1beta1Event.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
