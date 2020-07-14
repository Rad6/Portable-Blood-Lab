list="Handler User BloodExpert DailySchedule ServiceTime Order Lab LabPricingGate Prescription PrescriptionDetail TestList Test PaymentDetail PaymentGateway"

for i in $list; do
    file_name="$i".py
    touch $file_name
  echo "
class $i:
    pass
    " >> $file_name
done