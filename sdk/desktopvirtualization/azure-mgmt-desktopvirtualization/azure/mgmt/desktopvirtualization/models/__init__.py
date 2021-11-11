# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Application
    from ._models_py3 import ApplicationGroup
    from ._models_py3 import ApplicationGroupList
    from ._models_py3 import ApplicationGroupPatch
    from ._models_py3 import ApplicationList
    from ._models_py3 import ApplicationPatch
    from ._models_py3 import CloudErrorProperties
    from ._models_py3 import Desktop
    from ._models_py3 import DesktopList
    from ._models_py3 import DesktopPatch
    from ._models_py3 import ExpandMsixImage
    from ._models_py3 import ExpandMsixImageList
    from ._models_py3 import HostPool
    from ._models_py3 import HostPoolList
    from ._models_py3 import HostPoolPatch
    from ._models_py3 import Identity
    from ._models_py3 import LogSpecification
    from ._models_py3 import MSIXImageURI
    from ._models_py3 import MSIXPackage
    from ._models_py3 import MSIXPackageList
    from ._models_py3 import MSIXPackagePatch
    from ._models_py3 import MigrationRequestProperties
    from ._models_py3 import MsixPackageApplications
    from ._models_py3 import MsixPackageDependencies
    from ._models_py3 import OperationProperties
    from ._models_py3 import Plan
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResultWithSystemData
    from ._models_py3 import PrivateEndpointConnectionWithSystemData
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import RegistrationInfo
    from ._models_py3 import RegistrationInfoPatch
    from ._models_py3 import Resource
    from ._models_py3 import ResourceModelWithAllowedPropertySet
    from ._models_py3 import ResourceModelWithAllowedPropertySetIdentity
    from ._models_py3 import ResourceModelWithAllowedPropertySetPlan
    from ._models_py3 import ResourceModelWithAllowedPropertySetSku
    from ._models_py3 import ResourceProviderOperation
    from ._models_py3 import ResourceProviderOperationDisplay
    from ._models_py3 import ResourceProviderOperationList
    from ._models_py3 import ScalingHostPoolReference
    from ._models_py3 import ScalingPlan
    from ._models_py3 import ScalingPlanList
    from ._models_py3 import ScalingPlanPatch
    from ._models_py3 import ScalingSchedule
    from ._models_py3 import SendMessage
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import SessionHost
    from ._models_py3 import SessionHostHealthCheckFailureDetails
    from ._models_py3 import SessionHostHealthCheckReport
    from ._models_py3 import SessionHostList
    from ._models_py3 import SessionHostPatch
    from ._models_py3 import Sku
    from ._models_py3 import StartMenuItem
    from ._models_py3 import StartMenuItemList
    from ._models_py3 import SystemData
    from ._models_py3 import Time
    from ._models_py3 import UserSession
    from ._models_py3 import UserSessionList
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceList
    from ._models_py3 import WorkspacePatch
except (SyntaxError, ImportError):
    from ._models import Application  # type: ignore
    from ._models import ApplicationGroup  # type: ignore
    from ._models import ApplicationGroupList  # type: ignore
    from ._models import ApplicationGroupPatch  # type: ignore
    from ._models import ApplicationList  # type: ignore
    from ._models import ApplicationPatch  # type: ignore
    from ._models import CloudErrorProperties  # type: ignore
    from ._models import Desktop  # type: ignore
    from ._models import DesktopList  # type: ignore
    from ._models import DesktopPatch  # type: ignore
    from ._models import ExpandMsixImage  # type: ignore
    from ._models import ExpandMsixImageList  # type: ignore
    from ._models import HostPool  # type: ignore
    from ._models import HostPoolList  # type: ignore
    from ._models import HostPoolPatch  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import LogSpecification  # type: ignore
    from ._models import MSIXImageURI  # type: ignore
    from ._models import MSIXPackage  # type: ignore
    from ._models import MSIXPackageList  # type: ignore
    from ._models import MSIXPackagePatch  # type: ignore
    from ._models import MigrationRequestProperties  # type: ignore
    from ._models import MsixPackageApplications  # type: ignore
    from ._models import MsixPackageDependencies  # type: ignore
    from ._models import OperationProperties  # type: ignore
    from ._models import Plan  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResultWithSystemData  # type: ignore
    from ._models import PrivateEndpointConnectionWithSystemData  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import RegistrationInfo  # type: ignore
    from ._models import RegistrationInfoPatch  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceModelWithAllowedPropertySet  # type: ignore
    from ._models import ResourceModelWithAllowedPropertySetIdentity  # type: ignore
    from ._models import ResourceModelWithAllowedPropertySetPlan  # type: ignore
    from ._models import ResourceModelWithAllowedPropertySetSku  # type: ignore
    from ._models import ResourceProviderOperation  # type: ignore
    from ._models import ResourceProviderOperationDisplay  # type: ignore
    from ._models import ResourceProviderOperationList  # type: ignore
    from ._models import ScalingHostPoolReference  # type: ignore
    from ._models import ScalingPlan  # type: ignore
    from ._models import ScalingPlanList  # type: ignore
    from ._models import ScalingPlanPatch  # type: ignore
    from ._models import ScalingSchedule  # type: ignore
    from ._models import SendMessage  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import SessionHost  # type: ignore
    from ._models import SessionHostHealthCheckFailureDetails  # type: ignore
    from ._models import SessionHostHealthCheckReport  # type: ignore
    from ._models import SessionHostList  # type: ignore
    from ._models import SessionHostPatch  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import StartMenuItem  # type: ignore
    from ._models import StartMenuItemList  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import Time  # type: ignore
    from ._models import UserSession  # type: ignore
    from ._models import UserSessionList  # type: ignore
    from ._models import Workspace  # type: ignore
    from ._models import WorkspaceList  # type: ignore
    from ._models import WorkspacePatch  # type: ignore

from ._desktop_virtualization_api_client_enums import (
    ApplicationGroupType,
    ApplicationType,
    CommandLineSetting,
    CreatedByType,
    HealthCheckName,
    HealthCheckResult,
    HostPoolType,
    LoadBalancerType,
    Operation,
    PersonalDesktopAssignmentType,
    PreferredAppGroupType,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    PublicNetworkAccess,
    RegistrationTokenOperation,
    RemoteApplicationType,
    SSOSecretType,
    ScalingHostPoolType,
    ScalingScheduleDaysOfWeekItem,
    SessionHostLoadBalancingAlgorithm,
    SessionState,
    SkuTier,
    Status,
    StopHostsWhen,
    UpdateState,
)

__all__ = [
    'Application',
    'ApplicationGroup',
    'ApplicationGroupList',
    'ApplicationGroupPatch',
    'ApplicationList',
    'ApplicationPatch',
    'CloudErrorProperties',
    'Desktop',
    'DesktopList',
    'DesktopPatch',
    'ExpandMsixImage',
    'ExpandMsixImageList',
    'HostPool',
    'HostPoolList',
    'HostPoolPatch',
    'Identity',
    'LogSpecification',
    'MSIXImageURI',
    'MSIXPackage',
    'MSIXPackageList',
    'MSIXPackagePatch',
    'MigrationRequestProperties',
    'MsixPackageApplications',
    'MsixPackageDependencies',
    'OperationProperties',
    'Plan',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResultWithSystemData',
    'PrivateEndpointConnectionWithSystemData',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'RegistrationInfo',
    'RegistrationInfoPatch',
    'Resource',
    'ResourceModelWithAllowedPropertySet',
    'ResourceModelWithAllowedPropertySetIdentity',
    'ResourceModelWithAllowedPropertySetPlan',
    'ResourceModelWithAllowedPropertySetSku',
    'ResourceProviderOperation',
    'ResourceProviderOperationDisplay',
    'ResourceProviderOperationList',
    'ScalingHostPoolReference',
    'ScalingPlan',
    'ScalingPlanList',
    'ScalingPlanPatch',
    'ScalingSchedule',
    'SendMessage',
    'ServiceSpecification',
    'SessionHost',
    'SessionHostHealthCheckFailureDetails',
    'SessionHostHealthCheckReport',
    'SessionHostList',
    'SessionHostPatch',
    'Sku',
    'StartMenuItem',
    'StartMenuItemList',
    'SystemData',
    'Time',
    'UserSession',
    'UserSessionList',
    'Workspace',
    'WorkspaceList',
    'WorkspacePatch',
    'ApplicationGroupType',
    'ApplicationType',
    'CommandLineSetting',
    'CreatedByType',
    'HealthCheckName',
    'HealthCheckResult',
    'HostPoolType',
    'LoadBalancerType',
    'Operation',
    'PersonalDesktopAssignmentType',
    'PreferredAppGroupType',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
    'RegistrationTokenOperation',
    'RemoteApplicationType',
    'SSOSecretType',
    'ScalingHostPoolType',
    'ScalingScheduleDaysOfWeekItem',
    'SessionHostLoadBalancingAlgorithm',
    'SessionState',
    'SkuTier',
    'Status',
    'StopHostsWhen',
    'UpdateState',
]