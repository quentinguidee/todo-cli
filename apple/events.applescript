set duration to (read POSIX file "apple/duration") as integer
set event_name to (read POSIX file "apple/name")

set endDate to (current date)
set startDate to endDate - duration

tell application "Calendar"
    tell calendar "Work"
        make new event with properties {summary:event_name, start date:startDate, end date:endDate}
    end tell
end tell
