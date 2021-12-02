#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ar_marker_flexbe_states.get_ar_marker_pose_form_id_state import GetArMarkerPoseFromId
from miscellaneous_flexbe_states.message_state import MessageState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Nov 12 2021
@author: Gerard Harkema
'''
class ar_marker_test_idSM(Behavior):
	'''
	Tests the functionality of reading ar_mark list
	'''


	def __init__(self):
		super(ar_marker_test_idSM, self).__init__()
		self.name = 'ar_marker_test_id'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:474 y:60, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.id = 1

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('GetPoseFromId',
										GetArMarkerPoseFromId(),
										transitions={'done': 'MarkerMessage', 'not_found': 'failed', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'not_found': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'id': 'id', 'pose': 'pose'})

			# x:200 y:30
			OperatableStateMachine.add('MarkerMessage',
										MessageState(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
