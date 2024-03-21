# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys

from solution.consumer_sol import mqConsumer  # pylint: disable=import-error

def main(sector: str, queueName: str, stock: str, aditionalSectors: list[str]) -> None:
    
    # Implement Logic to Create Binding Key from the ticker and sector variable -  Step 2
    #
    #                       WRITE CODE HERE!!!
    #
    if not stock:
        bindingKey = "#.#." + sector
        bindingKey.strip()
    else:
        bindingKey = f"#.{stock}.{sector}"
        bindingKey.strip()
    if not aditionalSectors:
        consumer = mqConsumer(binding_key=bindingKey,exchange_name="Tech Lab Topic Exchange",queue_name=queueName)    
        consumer.startConsuming()
    else:
        consumer = mqConsumer(binding_key=bindingKey,exchange_name="Tech Lab Topic Exchange",queue_name=queueName)    
        consumer.startConsuming()
        # TODO: Finish this
    


if __name__ == "__main__":

    # Implement Logic to read the sector and queueName string from the command line and save them - Step 1
    #
    #                       WRITE CODE HERE!!!
    #
    if len(sys.argv) > 2:
        sector = sys.argv[2] if len(sys.argv) >0 else "error"
        queue = sys.argv[1] if len(sys.argv)>1 else "error"
        stock = sys.argv[3] if len(sys.argv)>2 else None
        aditionalSectors = sys.argv[4::] if len(sys.argv)>3 else None
    else:
        print("Usage: queueName sector [optional stock] [optional aditional sectors]")
    sys.exit(main(sector,queue, stock, aditionalSectors))
